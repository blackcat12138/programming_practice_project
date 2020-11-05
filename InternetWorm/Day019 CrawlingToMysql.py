'''
    [019]、爬取在线课程并存入Mysql数据库
    1.在mysql中创建用于存储爬取数据的表。如下sql语句：
        create table flask(
            productId bigint(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '商品ID',
            courseId bigint(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '课程ID',
            productName varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '课程名称',
            productType int(10) DEFAULT NULL COMMENT '商品类型',
            startTime varchar(23) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '开始时间',
            endTime varchar(23) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '结束时间',
            description text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '描述',
            provider varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '提供者',
            score float DEFAULT NULL COMMENT '成绩',
            scoreLevel int(11) DEFAULT NULL COMMENT '等级',
            learnerCount int(11) DEFAULT NULL COMMENT '学习总分',
            lessonCount int(11) DEFAULT NULL COMMENT '总课时',
            imgUrl varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'imgUrl',
            bigImgUrl varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'bigImgUrl',
            lectorName varchar(125) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '讲师名称',
            originalPrice float DEFAULT NULL COMMENT '原价'，
            PRIMARY KEY (`courseId`,`productId`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='爬虫网易课程网页';
    2.导入python的第三方相关模块
        pip install pymysql
        pip install requests
    3.首先使用requests模块发送POST请求,然后将接收到的数据转换成元组,
       将每页课程数据的元组存入到列表中,最后executemany()方法批量写入到数据库中。
'''
import time
from multiprocessing import Pool

import pymysql
import requests

# 连接数据库
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='root',
                       db='rpt_ods',
                       charset='utf8')  # 连接数据库
cur = conn.cursor()


def get_json(index):
    '''
    爬取课程的json数据
    :param index: 当前索引,从0开始
    :return: JSON数据
    '''
    url = 'https://study.163.com/p/search/studycourse.json'
    payload = {
        "activityId": 0,
        "keyword": "python",
        "orderType": 50,
        "pageIndex": 1,
        "pageSize": 50,
        "priceType": -1,
        "qualityType": 0,
        "relativeOffset": 0,
        "searchTimeType": -1,
    }
    headers = {
        "accept": "application/json",
        "host": "study.163.com",
        "content-type": "application/json",
        "origin": "https://study.163.com",
        "user-agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit "
                      "/537.36(KHTML, likeGecko)Chrome/87.0.4270.0Safari/537.36"
    }
    try:
        # 发送POST请求
        response = requests.post(url, json=payload, headers=headers)
        # 获取JSON数据
        content_json = response.json()
        if content_json and content_json['code']==0:
            return content_json
        return None
    except Exception as e:
        print('出错了')
        print(e)
        return None

def get_content(content_json):
    '''
    获取课程信息列表
    :param content_json: 获取的json格式数据
    :return: 课程数据
    '''
    if 'result' in content_json:
        return content_json['result']['list']


def check_course_exit(courseid):
    '''
    获取课程是否存在
    :param course_id:课程id
    :return: 课程存在返回True,否则返回False
    '''
    # 根据courseid查找flask表中记录
    sql = f'select courseid from rpt_ods.flask where courseid={courseid}'
    # 执行sql语句
    cur.execute(sql)
    # 查找一条记录
    course = cur.fetchone()
    # 若数据库中存在,返回True;否则,返回False
    if course:
        return True
    else:
        return False

def save_to_course(course_data):
    sql_course = """insert into flask values
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    # exetemany()方法插入多条记录
    cur.executemany(sql_course, course_data)


def save_mysql(content):
    course_data = []
    # 遍历课程列表
    for item in content:
            # 若数据表中没有该条记录,则保留
        if not check_course_exit(item['courseId']):
            course_value = (item['courseId'], item['productId'], item['productName'],
                            item['productType'], item['startTime'], item['description'],
                            item['provider'], item['endTime'], item['score'],
                            item['scoreLevel'], item['learnerCount'], item['lessonCount'],
                            item['imgUrl'], item['bigImgUrl'], item['lectorName'], item['originalPrice'])
            course_data.append(course_value)
    # 调用save_to_course方法,写入数据库
    save_to_course(course_data)

def main(index):
    # 获取JSON格式数据
    content_json = get_json(index)
    # 获取课程内容
    content = get_content(content_json)
    # 保存到数据库
    save_mysql(content)


if __name__ == '__main__':
    print('开始执行')
    start = time.time()
    # 获取总页数
    totle_Page_Count = get_json(1)["result"]["query"]["totlePageCount"]
    # 不使用多进程
    #for index in range(totle_Page_Count):
    #     main(index)
    # 为了提高效率,使用多进程
    pool=Pool()
    index =([x for x in range(totle_Page_Count)])
    pool.map(main,index)
    pool.close()
    pool.join()
    cur.close()
    conn.commit()
    conn.close()
    print('执行结束')
    end = time.time()
    print(f'程序执行时间是{end - start}秒')
