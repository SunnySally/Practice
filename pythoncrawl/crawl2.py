
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import os
import time
import csv

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("headless")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")
# browser = webdriver.Chrome(executable_path=DRIVER_BIN, options=option)
browser = webdriver.Chrome(executable_path=DRIVER_BIN)
browser.delete_all_cookies()

url = "https://www.whoscored.com/Players/106590/Histroy/Rafinha"

def get_url(url):
	browser.get(url)
	content = browser.page_source
	# remove comment
	html_doc = content.replace('<!--', '').replace('-->', '')
	soup = BS(html_doc, 'lxml')
	return soup


def write_csv(headers, lines):
	with open('test.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(headers)
		writer.writerows(lines)


def write_data(thead, tbody):
	h_rows = thead.contents[0].contents
	rows = tbody.contents[0:-1]
	lines = []
	headers = []

	for h in h_rows:
		if h.string.strip() == '':
			continue

		headers.append(h.string)

	for tr in rows:
		tds = tr.contents
		line = []

		for td in tds:
			if td.string is not None and td.string.strip() == '':
				continue

			if td.string is None and td['class'][0] == 'tournament':
				print(22222, td.contents[0].contents)
				line.append(td.contents[0].contents[1])
			else:
				print(222, td.string)
				line.append(td.string.strip())

		lines.append(line)

	write_csv(headers, lines)
	print(headers)
	print(lines)


count = 10


def get_data(url):

	try:
		# WebDriverWait(browser, 15, 0.5).until(EC.presence_of_element_located((By.ID, "top-player-stats-summary-grid")))


		# browser.find_element_by_id("agreed-too-cookies").click()
		# print(browser.find_element_by_id("agreed-too-cookies").click())

		# a = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, "top-player-stats-summary-grid")))
		browser.get(url)
		content = browser.page_source
		print(1, content)
		# print(2, a)
		# remove comment
		html_doc = content.replace('<!--', '').replace('-->', '')

		soup = BS(html_doc, 'lxml')
		table_container = soup.body.find(id='statistics-table-summary')
		thead = table_container.contents[0].contents[0]
		tbody = table_container.contents[0].contents[1]
		write_data(thead, tbody)
		browser.quit()
	except TimeoutException:
		print('not get data')
	finally:
		browser.quit()


get_data(url)

browser.quit()



