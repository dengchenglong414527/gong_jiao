import urllib.request
import time
import random
import os

from lxml import etree


def request_url(urllist):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    request = urllib.request.Request(url=urllist,headers=headers)
    content = urllib.request.urlopen(request).read().decode('utf8')
    return content


def jiexineirong(content):
    tree = etree.HTML(content)
    divlist = tree.xpath('//div[@id="container"]/div/div/a/img')

    filepath = os.path.dirname(os.path.abspath(__file__)) + '\\性感美女'

    for i in divlist:
        img = i.xpath('@src2')
        title = i.xpath('@alt')
        # print(img[0])   'http://pic2.sc.chinaz.com/Files/pic/pic9/201810/zzpic14638_s.jpg'

        if not os.path.exists(filepath):

            os.makedirs(filepath)

        file_suffix = os.path.splitext(img[0])[1]

        # file_name = str(random.randint(0, 999999))

        filename = '{}{}{}{}'.format(filepath,os.sep,title[0],file_suffix)

        urllib.request.urlretrieve(img[0], filename=filename)
        time.sleep(1)
        print('保存完...{} !! '.format(title[0]))

def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian{}.html'

    start_page = int(input('起始页：'))
    end_page = int(input('结束页：'))
    for page in range(start_page , end_page + 1 ):
        if page == 1:
            print('正在下载第{}页......'.format(page))
            time.sleep(2)
            urllist = url.format('')
        else:

            print('正在下载第{}页......'.format(page))
            time.sleep(2)
            urllist = url.format('_{}'.format(page))

        # 发送请求_获取响应内容
        content = request_url(urllist)
        # print(content)

        # 解析内容 获得图片 标题
        jiexineirong(content)

if __name__ == '__main__':
    main()
