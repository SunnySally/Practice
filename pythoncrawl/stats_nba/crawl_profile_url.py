# import requests
# from bs4 import BeautifulSoup as BS
from lxml import etree
from selenium import webdriver
import os
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv

# 修改页面加载策略，不等待解析完成，会selenium会直接返回
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

option = webdriver.ChromeOptions()
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")
browser = webdriver.Chrome(executable_path=DRIVER_BIN, options=option)
url = 'https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&Season=2018-19&SeasonType=Regular%20Season'

headers = ['idx', 'name', 'url']
lines = []


def write_csv(title, headers, lines):
    filename = 'nba/' + title+'.csv'
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(lines)
    print(title, ' is written')

try:
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]')))
    browser.execute_script("window.stop();")

    html_doc = browser.page_source
    html_doc = html_doc.replace('<!--', '').replace('-->', '')

    html = etree.HTML(html_doc)

    trs = html.xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody//tr')

    cnt = 0
    for tr in trs:
        tds = tr.xpath('.//td')
        line = []
        for i, td in enumerate(tds):
            if i == 1:
                line.append(cnt)
                line.append(td.xpath('./a/text()')[0])
                line.append(td.xpath('./a/@href')[0])
                cnt = cnt+1
        lines.append(line)

    write_csv('url', headers, lines)

finally:
    browser.quit()

