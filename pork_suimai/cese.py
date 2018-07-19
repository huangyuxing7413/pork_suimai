import requests     # requests是python的一个轻量级爬虫框架
import os       # python的文件操作库
from bs4 import BeautifulSoup as bs  # BeautifulSoup这个名字太长了，简写成bs
from lxml import etree  # 这是xpath解析库

def get_response(url): # 打开网页函数
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    response = requests.get(url, headers)
    response.encoding = 'gbk'

    return response

'''
def xpath_href_content(base_url,url,rule_str):
    response = get_response(url)
    links = []
    html = etree.HTML(response.content)
    content = html.xpath(rule_str + 'text()')
    hrefs = html.xpath(rule_str + '@href')
    for i in hrefs:
        links.append(base_url + i )
    return content,links
'''
def xpath_href_content(base_url,url,rule_str):
    response = get_response(url)
    books = {}
    html = etree.HTML(response.content)
    content = html.xpath(rule_str + 'text()')
    hrefs = []

    #hrefs = html.xpath(rule_str + '@href')
    for i in html.xpath(rule_str + '@href'):
        hrefs.append(base_url + i)

    books = dict(zip(content, hrefs))
    return books


def get_content(title_link):
    response = get_response(title_link)
    soup = bs(response.text, 'html.parser')
    content = soup.find('div', class_='nr_con').strings
    # strings属性返回div标签下所有子标签的string

    return content

def main():    # 主函数
    base_url = 'https://www.gulongwang.com'
    books = xpath_href_content(base_url,base_url,'//*[@id="right"]/ul/li/p/a/')
    books = xpath_href_content(base_url,base_url,'//*[@id="right"]/div/div[2]/ul/li/a/')

    print(books)
# 当.py文件运行时，在if __name__ == "__main__":下的的代码将会运行
# 当该文件被当成模块运行时，if __name__ == "__main__":下的代码不会被运行
if __name__ == "__main__":
    main()
