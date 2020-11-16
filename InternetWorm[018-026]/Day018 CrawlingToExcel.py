'''
    [018]、爬取在线课程并保存到Excel
    实现步骤：
        1.进入网易云课堂python课程页面（https://study.163.com/courses-search?keyword=python）
            (a).进入页面后,点击右键选择检查
            (b).在开发者调试页面中
                选择Network选项-->刷新页面
                -->Name栏查找并选择.json结尾文件(studycourse.json)
                -->复杂Headers栏中的内容
        2.安装第三方模块requests和xlsxwriter两个模块后进行导入
            pip install requests
            pip install xlsxwriter
         在dos窗口执行上面命令后,pycharm工具需要加入模块
            File-->settings-->project:pythonDemo-->python Interpreter
        3.使用requests模块发送post请求,获取页面信息,然后json()方法获取json格式数据。
        4.最后使用xlsxwriter模块将获取的数据写入到Excel文件中,随后依次遍历每页的数据。
'''

import requests
import xlsxwriter
from xlsxwriter import worksheet


def get_json(index):
    '''
    抓取课程的json数据
    :param index: 当前索引,从0开始
    :return: json数据
    '''
    url = "https://study.163.com/p/search/studycourse.json"
    # Payload信息
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
    # headers信息
    headers = {
        "accept": "application/json",
        "host": "study.163.com",
        "content-type": "application/json",
        "origin": "https://study.163.com",
        "user-agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit "
                      "/537.36(KHTML, likeGecko)Chrome/87.0.4270.0Safari/537.36"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)  # 发送post请求
        content_json = response.json()                                # 获取json数据
        if content_json and content_json["code"] == 0:                # 判断数据是否存在
            return content_json
        return None
    except Exception as e:
        print('wrong')
        print(e)
        return None


def get_content(content_json):
    '''
    获取课程信息列表
    :param content_json:获取的json格式数据
    :return:课程数据
    '''
    if "result" in content_json:
        return content_json["result"]["list"]  # 返回课程数据列表


def save_excel(content, index):
    '''
    存储到Excel
    :param content: 课程内容
    :param index: 索引值,从0开始
    :return: None
    '''
    for num, item in enumerate(content):
        row = 50 * index + (num + 1)
        # 行内容
        worksheet.write(row, 0, item['productId'])
        worksheet.write(row, 1, item['courseId'])
        worksheet.write(row, 2, item['productName'])
        worksheet.write(row, 3, item['productType'])
        worksheet.write(row, 4, item['startTime'])
        worksheet.write(row, 5, item['endTime'])
        worksheet.write(row, 6, item['description'])
        worksheet.write(row, 7, item['provider'])
        worksheet.write(row, 8, item['score'])
        worksheet.write(row, 9, item['scoreLevel'])
        worksheet.write(row, 10, item['learnerCount'])
        worksheet.write(row, 11, item['lessonCount'])
        worksheet.write(row, 12, item['imgUrl'])
        worksheet.write(row, 13, item['bigImgUrl'])
        worksheet.write(row, 14, item['lectorName'])
        worksheet.write(row, 15, item['originalPrice'])


def main(index):
    '''
    程序运行函数
    :param index: 索引值,从0开始
    :return:
    '''
    content_json = get_json(index)
    content = get_content(content_json)
    save_excel(content, index)


if __name__ == '__main__':
    print('开始执行')
    workbook = xlsxwriter.Workbook("网易云课堂爬取课程数据.xlsx")       # 创建excel
    worksheet = workbook.add_worksheet("first_sheet")                # 创建sheet
    worksheet.write(0, 0, '商品ID')
    worksheet.write(0, 1, '课程ID')
    worksheet.write(0, 2, '商品名称')
    worksheet.write(0, 3, '商品类型')
    worksheet.write(0, 4, '开始时间')
    worksheet.write(0, 5, '结束时间')
    worksheet.write(0, 6, '描述')
    worksheet.write(0, 7, '提供者')
    worksheet.write(0, 8, '得分')
    worksheet.write(0, 9, '分级')
    worksheet.write(0, 10, '学习总分')
    worksheet.write(0, 11, '总课时')
    worksheet.write(0, 12, 'imgUrl')
    worksheet.write(0, 13, 'bigImgUrl')
    worksheet.write(0, 14, '讲师名称')
    worksheet.write(0, 15, '原价')
    totlePageCount = get_json(1)['result']['query']['totlePageCount'] # 获取行总页数
    # 遍历每一页
    for index in range(totlePageCount):
        main(index)
        workbook.close()
        print('执行结束')
