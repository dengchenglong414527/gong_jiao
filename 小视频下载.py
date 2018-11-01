'''
梨视频  下载
'''

import os
import time
import re
import random
import requests
import urllib.request
from lxml import etree

url = 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=31&start={}'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
}

start_page= int(input('起始页：'))
end_page = int(input('结束页：'))
if start_page == 0 or end_page == 0:
    print('起始页或结束页不能为 0 ！！ ... 请再次操作.....')
    exit()

# filepath = r'C:\Users\dengc\Desktop\梨视频'
filepath = os.path.dirname(__file__)
filename = filepath + '/梨视频'

for page in range(start_page , end_page + 1 ):
    if  start_page == 0:
        urllist = url.format(12)
    else:
        urllist = url.format(page * 12)
    # print(urllist)
    time.sleep(5)
    r = requests.get(url=urllist,headers=headers)
    tree = etree.HTML(r.text)
    # a = tree.xpath('//li[@class="categoryem"]//a/@href')
    a = tree.xpath('//li/div/a/@href')
    for u in a:
        img_url = 'http://www.pearvideo.com/' + u
        # print(img_url)
        time.sleep(5)

        v_list = requests.get(url=img_url, headers=headers)
        pattern = re.compile(r'srcUrl="(.*?)",')
        ret = pattern.search(v_list.text)
        asd = ret.group(1)

        if not os.path.exists(filename):
            os.mkdir(filename)

        file_name = random.randint(1,10000)

        fname = os.path.join(filename,str(file_name)+'.mp4')

        urllib.request.urlretrieve(asd,fname)

        print('{}下载成功...'.format(str(file_name)))
        time.sleep(5)








