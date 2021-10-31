# import re
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.embassy-worldwide.com/embassy/angolan-consulate-general-in-mongu-zambia/'
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
#
# # response = requests.get(url)
# # soup = BeautifulSoup(response.text, 'lxml') # Make xml from the html
#
# soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
#
# print(soup.text)
# links = re.findall(r"https://www.embassy-worldwide.com/country/[a-z0-9\.\-+_]+\"", soup.text)
#
# print(links)

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from bs4 import BeautifulSoup

import csv

#driver = webdriver.Chrome()
#driver.get('https://www.embassy-worldwide.com/')
###########################################################
# url = 'https://www.embassypages.com/'
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# driver = webdriver.Chrome(options=options)
# driver.get(url)
# sleep(10)
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')
#
# list = []
#
# for col in soup.find_all('div', 'col2'):
#     for cou in col.find_all('a'):
#         list.append(cou.get('href'))
#
# df = pd.DataFrame(list)
# df.to_csv('list_countries.csv', index=False)
###########################################################

###########################################################
url = 'https://www.embassypages.com/'
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.get(url)
sleep(10)
with open('list_countries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for each in row:
            if each != '0':
                driver.get(url + each)
                sleep(10)
###########################################################