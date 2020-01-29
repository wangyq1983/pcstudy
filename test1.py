import requests
import bs4
import logging
res = requests.get('https://bbs.hupu.com/vote')

try:
    res.raise_for_status()
    exeres = bs4.BeautifulSoup(res.text, 'lxml')
    forexe = exeres.select('.truetit')
    playFile = open("vote.txt", "w", encoding="utf-8")
    for ab in forexe:
        print(type(ab.getText()))
        playFile.write(ab.getText()+"\n")

    # for chunk in res.iter_content(100000):
    #     playFile.write(chunk)
    playFile.close()
except:
    pass
