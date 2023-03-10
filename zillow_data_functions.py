# -*- coding: utf-8 -*-
"""Zillow_Data_Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DN96YGsTTri0TzMNSorl9YevkH34urGK
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import datetime 
import csv

URL = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-117.91235374414063%2C%22east%22%3A-116.30560325585938%2C%22south%22%3A32.36072020501597%2C%22north%22%3A33.28623992760275%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A4000%7D%2C%22price%22%3A%7B%22max%22%3A851039%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22sort%22%3A%7B%22value%22%3A%22size%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%7D%7D'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

print(soup2)

price = soup2.find('span', {'data-test':'property-card-price'}).text.strip()
print(price)

data_test = soup2.find_all('div', class_='StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0 wgiFT')
for item in data_test:
    print(item.text.strip())

