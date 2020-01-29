import requests
import os
from lxml import etree

url = "https://xkcd.com/"

dir = 'D:\\python\\xkcd'

if os.path.exists(dir):
    pass
else:
    os.mkdir(dir)

total = range(10)

for num in total:
    if num == 0:
        pass
    else:
        newurl = url + str(num)
        print('downloading page %s...' % newurl)
        res = requests.get(newurl)
        res.raise_for_status()
        html = etree.HTML(res.text)
        # xpath返回列表序号从0开始
        resultImg = html.xpath("//div[@id='comic']/img/@src[1]")
        # 列表转字符
        resultImgurl = 'https:'+''.join(resultImg)
        # print(str(resultImg))
        imgres = requests.get(resultImgurl)
        imgres.raise_for_status()
        imgfile = open(os.path.join(
            'xkcd', os.path.basename(resultImgurl)), 'wb')
        for chunk in imgres.iter_content(100000):
            imgfile.write(chunk)
        imgfile.close()
