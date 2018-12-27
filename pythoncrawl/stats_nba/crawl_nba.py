from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree
import csv
import time
import os
from pprint import pprint

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "../bin/chromedriver")
# XPATH = '/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table[1]/div[2]/div[1]/table'
XPATH = '/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table[2]/div[2]/div[1]/table'
URL_PREFIX = 'https://stats.nba.com'
MAX_TIMEOUT = 10
DIR = 'data/advanced'

success_lst = []
failure_lst = []

# 修改页面加载策略，不等待解析完成，selenium会直接返回
#caps["pageLoadStrategy"] = "normal"  #  complete
#caps["pageLoadStrategy"] = "eager"  #  interactive
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

def write_csv(table, filename):
    headers = table[0].xpath('./thead/tr//th/text()')
    if headers[-1:][0] != 'PIE':
        raise Exception('wrong table')
    trs = table[0].xpath('./tbody//tr')
    all_lines = []
    for tr in trs:
        line = []
        tds = tr.xpath('.//td')
        for idx, td in enumerate(tds):
            if idx == 1 and len(td.xpath('./a/text()')) > 0:
                line.append(td.xpath('./a/text()')[0])
            else:
                line.append(td.xpath('./text()')[0])
        all_lines.append(line)

    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(all_lines)

def crawl_single(driver, idx, url, name):
    ret = False
    timeout_cnt = 0
    while ret == False and timeout_cnt <= MAX_TIMEOUT:
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATH))
            )

            html_doc = driver.page_source
            html_doc = html_doc.replace('<!--', '').replace('-->', '')

            html = etree.HTML(html_doc)
            table = html.xpath(XPATH)

            write_csv(table, os.path.join(DIR, '%d-' % idx + name + '.csv'))

            ret = True
        # catch any error
        except:
            timeout_cnt += 1
            print(idx, name, 'timeout %d' % timeout_cnt)
            ret = False
        driver.execute_script("window.stop();")

    if ret:
        success_lst.append((idx, url, name))
    else:
        failure_lst.append((idx, url, name))



def main():
    driver = webdriver.Chrome(executable_path=DRIVER_BIN)
    downloaded_files = set(filename[:-4] for filename in os.listdir(DIR))
    print("%d already downloaded" % len(downloaded_files))

    with open('./nba/url.csv') as csvfile:
        csvdata = csv.DictReader(csvfile)
        for idx, row in enumerate(csvdata):
            if ('%d-' % idx + row['name']) not in downloaded_files:
                time.sleep(0.5)
                print(idx, row['name'], row['url'])
                crawl_single(driver, idx, URL_PREFIX + row['url'], row['name'])

    pprint(success_lst)
    pprint(failure_lst)

if __name__ == '__main__':
    main()
