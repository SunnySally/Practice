# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error
import re
from bs4 import BeautifulSoup
import xlwt
import chardet
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码


def askURL(url):
    try:
        response = request.urlopen(url)
        originHtml = response.read()
        charset = chardet.detect(originHtml)
        html = originHtml.decode(charset['encoding'])
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def getData(baseurl):
    findLink = re.compile(r'<a href="(.*?)">')
    findImgSrc = re.compile(r'<img.*src="(.*jpg)"', re.S)
    findTitle = re.compile(r'<span class="title">(.*)</span>')
    findRating = re.compile(
        r'<span class="rating_num" property="v:average">(.*)</span>')
    findJudge = re.compile(r'<span>(\d*)人评价</span>')
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
    remove = re.compile(r'                            |\n|</br>|\.*')
    datalist = []
    for i in range(0, 10):
        url = baseurl+str(i*25)
        html = askURL(url)
        soup = BeautifulSoup(html, 'lxml')
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace(' / ', '')
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('没有英文名')
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace('。', '')
                data.append(inq)
            else:
                data.append('没有影评')
            bd = re.findall(findBd, item)[0]
            # print(bd)
            bd = re.sub(remove, '', bd)
            # print(bd)
            bd = re.sub('<br/>', ' ', bd)  # 去掉<br>
            bd = re.sub('/', ' ', bd)
            bd = re.sub('[a-zA-Z]', ' ', bd)
            # data.append(bd)
            bdlist= []
            word = bd.split(' ')
            for s in word:
                if len(s) != 0 and s != ' ':
                    bdlist.append(s)
            for i in range(0, 7):
                try:
                    print(i)
                    bdlist[i]
                except IndexError:
                    bdlist.append('没有数据')
            switcher = {
                1: bdlist[1],
                3: bdlist[3],
                4: bdlist[4],
                5: bdlist[5],
                6: bdlist[6],
            }
            for i in switcher:
                print(i)
                data.append(switcher[i])
            datalist.append(data)
        return datalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ['电影详情链接', '图片链接', '影片中文名', '影片外国名', '评分',
           '评价数', '概况', '导演', '主演', '年份', '地区', '类别']
    for i in range(len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, 20):
        data = datalist[i]
        for j in range(len(col)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


def main():
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    savepath = 'D:/python/movieTop250.xlsx'
    saveData(datalist, savepath)


main()
