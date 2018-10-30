import requests
from lxml import etree
import time
url = 'http://zhengzhou.8684.cn'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }
def lu_request(lu_url,fp):
    nu = requests.get(url=lu_url,headers=headers)
    content = etree.HTML(nu.text)
    con = content.xpath('//div[@class="bus_i_content"]')
    for div in con:
        biaoti = div.xpath('div[@class="bus_i_t1"]/h1/text()')[0]
        run_time = div.xpath('p[1]/text()')[0]
        piaojia = div.xpath('p[2]/text()')[0]
        zhandianxinxi = div.xpath('//div[@class="bus_line_site "]/div//a/text()')
        item = {
            '标题':biaoti,
            '运行时间':run_time,
            '票价':piaojia,
            '站点':zhandianxinxi,
        }
        fp.write(str(item) + '\n' + '\n')


def number_request(numurl,fp):
    n = requests.get(url=numurl,headers=headers)
    tre = etree.HTML(n.text)
    lu_list = tre.xpath('//div[@id="con_site_1"]/a/@href')
    for lu in lu_list:
        print('正在下载第{}页'.format(lu))
        time.sleep(2)
        lu_url = url + lu

        # 数字抬头获取内容
        lu_request(lu_url,fp)



def main():
    r = requests.get(url=url,headers=headers)
    # string = r.text
    tree = etree.HTML(r.text)
    num_list = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
    fp = open('郑州数字公交.txt','w',encoding='utf8')
    for num in num_list:
        print('正在下载第{}页'.format(num))
        time.sleep(2)
        # 拼接数字开头的url
        numurl = url + num

        # 发送请求获取数字开头的公交信息url
        number_request(numurl,fp)

if __name__ == '__main__':
    main()