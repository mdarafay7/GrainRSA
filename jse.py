#!/usr/bin/python

import bs4 as bs
import urllib.request
import csv
import pymysql
import re
import requests
from datetime import date
import automata as auto
import dbmanager as dbm

url = "https://www.fin24.com"
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
html=page.content;

tree = bs.BeautifulSoup(html)
good_html = tree.prettify()
soup = bs.BeautifulSoup(good_html,"html.parser")
stock_info=soup.find("div",class_='stock_items')

allshare = stock_info.find(title='All Share')
allshare=allshare.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
jse_all_share=list(allshare.children)[3]
print(jse_all_share.get_text())
jse_all_share_float=auto.str_to_float_jse(jse_all_share.get_text())

gold=soup.find(title='Gold')
gold=gold.next_element.next_element.next_element.next_element.next_element.next_element
jse_gold=list(gold.children)[3]
print(jse_gold.get_text())
jse_gold_float=auto.str_to_float_jse(jse_gold.get_text())

indutop40=soup.find(title='Top 40')
indutop40=indutop40.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
jse_indutop40=list(indutop40.children)[3]
print(jse_indutop40.get_text())
jse_indutop40_float=auto.str_to_float_jse(jse_indutop40.get_text())

zar_usd=soup.find(title='ZAR/USD')
zar_usd=zar_usd.next_element.next_element.next_element.next_element.next_element.next_element
#print(list(zar_usd.children))
jse_zar_usd=list(zar_usd.children)[3]
print(jse_zar_usd.get_text())
jse_zar_usd_float=auto.str_to_float_jse(jse_zar_usd.get_text())

GOLD=soup.find(title='Gold')
GOLD=GOLD.next_element.next_element.next_element.next_element.next_element.next_element
GOLD=list(GOLD.children)[3]
print(GOLD.get_text())
GOLD_float=auto.str_to_float_jse(GOLD.get_text())

ZAR_EUR=soup.find(title='ZAR/EUR')
ZAR_EUR=ZAR_EUR.next_element.next_element.next_element.next_element.next_element.next_element
ZAR_EUR=list(ZAR_EUR.children)[3]
print(ZAR_EUR.get_text())
ZAR_EUR_float=auto.str_to_float_jse(ZAR_EUR.get_text())

ZAR_GBP=soup.find(title='ZAR/GBP')
ZAR_GBP=ZAR_GBP.next_element.next_element.next_element.next_element.next_element.next_element
ZAR_GBP=list(ZAR_GBP.children)[3]
print(ZAR_GBP.get_text())
ZAR_GBP_float=auto.str_to_float_jse(ZAR_GBP.get_text())

BRENT_OIL=soup.find(title='Oil')
BRENT_OIL=BRENT_OIL.next_element.next_element.next_element.next_element.next_element.next_element
BRENT_OIL=list(BRENT_OIL.children)[3]
print(BRENT_OIL.get_text())
BRENT_OIL_float=auto.str_to_float_jse(BRENT_OIL.get_text())



todays_date=date.today()
todays_date_str=date.isoformat(todays_date)

db = pymysql.connect(host="localhost",user="root",password="test123",db="TESTDB" )
cursor = db.cursor()
dbm.jse_DB()


sql = "INSERT INTO GENERAL_INFORMATION(DATE, \
      JSE_ALL_SHARE,JSE_INDU,JSE_GOLD,ZAR_USD,GOLD,ZAR_EUR,ZAR_GBP,BRENT_OIL)\
      VALUES ('%s', '%f', '%f', '%f','%f','%f','%f','%f','%f')" % \
      (todays_date_str,jse_all_share_float,jse_indutop40_float,jse_gold_float,jse_zar_usd_float,GOLD_float,ZAR_EUR_float,ZAR_GBP_float,BRENT_OIL_float)
#     data2.clear()
#
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
#
#
#     data.append(string)
#
# with open('data.csv', 'w+') as writeFile:
#     writer = csv.writer(writeFile)
#     for word in data:
#         writer.writerow([word])
#
# writeFile.close()
#
db.close()
