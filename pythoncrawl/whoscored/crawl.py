
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import os
import time
import csv

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
# option.add_argument("headless")

# option.add_argument("--proxy-server=http://115.46.64.250:8123")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")
browser = webdriver.Chrome(executable_path=DRIVER_BIN, options=option)

url = 'https://www.whoscored.com/Statistics'

url_list = [
	# 'https://www.whoscored.com/Players/108226/Show/Mohamed-Salah',
	# 'https://www.whoscored.com/Players/22221/Show/Luis-Su%C3%A1rez',
	# 'https://www.whoscored.com/Players/14102/Show/David-Silva',
	# 'https://www.whoscored.com/Players/41330/Show/Marco-Reus',
	# 'https://www.whoscored.com/Players/83390/Show/Lorenzo-Insigne',
	# 'https://www.whoscored.com/Players/70087/Show/Stephan-El-Shaarawy',
	# 'https://www.whoscored.com/Players/29400/Show/Robert-Lewandowski',
	# 'https://www.whoscored.com/Players/23110/Show/%C3%81ngel-Di-Mar%C3%ADa',
	# 'https://www.whoscored.com/Players/109915/Show/Sadio-Man%C3%A9',
	# 'https://www.whoscored.com/Players/83532/Show/Harry-Kane'
	# 'https://www.whoscored.com/Players/80241/Show/Antoine-Griezmann',
	# 'https://www.whoscored.com/Players/44120/Show/Pierre-Emerick-Aubameyang',
	# 'https://www.whoscored.com/Players/73078/Show/Alexandre-Lacazette',
	# 'https://www.whoscored.com/Players/14296/Show/Karim-Benzema',
	# 'https://www.whoscored.com/Players/78498/Show/Romelu-Lukaku',
	# 'https://www.whoscored.com/Players/78498/Show/Romelu-Lukaku',
	# 'https://www.whoscored.com/Players/91213/Show/%C3%81lvaro-Morata',
	# 'https://www.whoscored.com/Players/19729/Show/Gonzalo-Higua%C3%ADn',
	# 'https://www.whoscored.com/Players/106981/Show/Jamie-Vardy',
	# 'https://www.whoscored.com/Players/92812/Show/Kevin-Volland',
	# 'https://www.whoscored.com/Players/13812/Show/Gareth-Bale',
	# 'https://www.whoscored.com/Players/96182/Show/Roberto-Firmino',
	# 'https://www.whoscored.com/Players/37099/Show/Thomas-M%C3%BCller',
	# 'https://www.whoscored.com/Players/279379/Show/Gabriel-Jesus',
	# 'https://www.whoscored.com/Players/96449/Show/Julian-Draxler',
	# 'https://www.whoscored.com/Players/13756/Show/Mesut-%C3%96zil',
	# 'https://www.whoscored.com/Players/134893/Show/Nabil-Fekir'
]

def get_url(url, id):
	browser.get(url)
	WebDriverWait(browser, 5, 0.5).until(EC.presence_of_element_located((By.ID, id)))
	content = browser.page_source
	# remove comment
	html_doc = content.replace('<!--', '').replace('-->', '')
	soup = BS(html_doc, 'lxml')
	return soup


def write_csv(title, headers, lines):
	filename = 'playerdata/' + title+'.csv'
	with open(filename, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(headers)
		writer.writerows(lines)
	print(title, ' is written')


def process_data(title, thead, tbody):
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
				line.append(td.contents[0].contents[1])
			else:
				line.append(td.string.strip())

		lines.append(line)

	write_csv(title, headers, lines)


def get_data(url):
	url = url.replace('Show', 'History')
	index = url.find('History')
	title = url[index+8:]

	doc = get_url(url, 'top-player-stats-summary-grid')
	table_container = doc.body.find(id='statistics-table-summary')
	thead = table_container.contents[0].contents[0]
	tbody = table_container.contents[0].contents[1]
	process_data(title, thead, tbody)


def get_urlist(url):
	doc = get_url(url, 'top-player-stats-summary-grid')
	table_container = doc.body.find(id='statistics-table-summary')
	tbody = table_container.contents[0].contents[1]
	trs = tbody.contents
	urls = []

	for tr in trs:
		urls.append('https://www.whoscored.com' + tr.contents[3].contents[0]['href'])

	return urls


# urls = get_urlist(url)

for url in url_list:
	time.sleep(0.5)
	get_data(url)

browser.quit()
