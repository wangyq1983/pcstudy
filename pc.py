import requests
import os
from lxml import etree
import json
url = 'https://bbs.hupu.com/vote'
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
}
reponse = requests.get(url, headers=headers)
reponse.encoding = 'utf-8'


# 拿到获取的数据再处理
html = etree.HTML(reponse.text)
resultTitle = html.xpath("//li/div/a[@class='truetit']//text()")
resultAuth = html.xpath("// a[@class='aulink']")
resultTime = html.xpath("// li/div[@class='author box']/a[2]")
try:
    os.mkdir('hupu')
except os.error:
    pass
os.chdir('hupu')
fd = open('hupu1.txt', 'w', encoding="utf-8")
for title in resultTitle:
    print(title)
    fd.write(title + "\n")
fd.close()
