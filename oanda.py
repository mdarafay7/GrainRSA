import bs4 as bs
import urllib.request
import csv
import pymysql
import re
import requests
from datetime import date
import automata as auto
import dbmanager as dbm

url = "https://www1.oanda.com/currency/live-exchange-rates/"
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
html=page.content;

tree = bs.BeautifulSoup(html)
good_html = tree.prettify()
soup = bs.BeautifulSoup(good_html,"html.parser")
