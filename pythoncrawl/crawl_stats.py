import requests
# from bs4 import BeautifulSoup as BS
from lxml import etree
from selenium import webdriver
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")
browser = webdriver.Chrome(executable_path=DRIVER_BIN, options=option)


url = 'https://stats.nba.com/team/1610612749/onoffcourt-traditional/'
browser.get(url)
# WebDriverWait(browser, 5, 0.5).until(EC.presence_of_element_located(By.XPATH, '//nba-stat-table'))
print('5555')
# html_doc = browser.page_source
# html_doc = html_doc.replace('<!--', '').replace('-->', '')
# soup = BS(html_doc, 'lxml')
# contents = soup.find_all('div', class_='nba-stat-table')
#
# for content in contents:
#     table = content.find()
#
#
#
# # for table in content.
# print('111')
# print(contents.length)

browser.quit()
