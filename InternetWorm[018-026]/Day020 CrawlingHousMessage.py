'''
    [020]、爬取北上广租房信息
    1.要求:爬取租房信息后,将自动生成对应城市名称的租房信息csv文件
    2.实现步骤：
        (a).首先分析各个城市的租房网页地址,获取当前城市租房信息的总页数。
            打开链家网首页地址(https://sz.lianjia.com/)
                北京 --> https://bj.lianjia.com/zufang/rt200600000001/
                上海 --> https://sh.lianjia.com/zufang/rt200600000001/
                广州 --> https://gz.lianjia.com/zufang/rt200600000001/
            当单击下一页,观察网页地址中页面位置和规律,如下:
                https://bj.lianjia.com/zufang/pg2rt200600000001/#contentList
        (b).再根据总页数循环遍历爬取每页中所需要的租房信息,最后将信息整合并写入csv文件中。
'''
from xml import etree

import aiohttp
import requests


class UserAgent(object):
    def __init__(self):
        self.random = None

    pass


# 链家爬虫类
class HomeSpider():
    # __init()方法用于保存数据的列表
    def __init__(self):
        # 创建数据列表
        self.data = []
        # 通过UserAgent().random随机生成浏览器头部信息
        self.headers = {"User-Agent": UserAgent().random}

    # 异步网络请求的方法
    async def request(self, url):
        # 创建异步网络请求对象
        async with aiohttp.ClientSession()as session:
            try:
                # 根据传递的地址发送网络请求
                async with session.get(url, headers=self.headers, timeout=3) as response:
                    print(response.status)
                    # 若请求码为200表示请求成功
                    if response.status == 200:
                        # 获取请求结果中的文本代码
                        result = await response.text()
                        return result
            except Exception as e:
                print(e.args)

    # 请求一次,获取租房信息的所有页码
    def get_page_all(self, city):
        # 获取城市对应的字母
        city_letter = self.get_city_letter(city)
        url = 'https://{}.lianjia.com/zufang/{}rt200600000001/#contentList'.format(city_letter, city)
        # 发送网络请求
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            # 创建一个XPath解析对象
            html = etree.HTML(response.text)
            # 获取租房信息的所有页码
            page_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/p[1]/a')[0]
            print('租房信息总页码获取成功！')
            return int(page_all) + 1
        else:
            print('获取租房信息所有页码的请求未成功！')

    # 获取城市所对应的英文字母
    def get_city_letter(self, city_name):
        city_dict = {'北京': 'bj', '上海': 'sh', '广州': 'gz'}
        # 返回城市名称对应的英文字母
        return city_dict.get(city_name)


if __name__ == '__main__':
    input_city = input('请输入需要下载租客信息的城市名称！')
    # 创建爬虫类对象
    home_spider = HomeSpider
    # 获取所有页码
    page_all = home_spider.get_page_all(input_city)
    print(page_all)
