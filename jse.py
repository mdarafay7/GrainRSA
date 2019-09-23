#!/usr/bin/python

import bs4 as bs
import urllib.request
import csv
import pymysql
import re
import requests
from datetime import date

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

gold=soup.find(title='Gold')
gold=gold.next_element.next_element.next_element.next_element.next_element.next_element
jse_gold=list(gold.children)[3]
print(jse_gold.get_text())


indutop40=soup.find(title='Top 40')
indutop40=indutop40.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
jse_indutop40=list(indutop40.children)[3]
print(jse_indutop40.get_text())

zar_usd=soup.find(title='ZAR/USD')
zar_usd=zar_usd.next_element.next_element.next_element.next_element.next_element.next_element
#print(list(zar_usd.children))
jse_zar_usd=list(zar_usd.children)[3]
print(jse_zar_usd.get_text())





todays_date=date.today()
todays_date_str=date.isoformat(todays_date)

db = pymysql.connect(host="localhost",user="root",password="RAFay786$",db="TESTDB" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS GENERAL_INFORMATION");
sql = """CREATE TABLE GENERAL_INFORMATION (
    DATE  VARCHAR(20) NOT NULL,
    JSE_ALL_SHARE FLOAT(20),
    JSE_INDU FLOAT(20),
    JSE_GOLD FLOAT(20),
    RAND_US_Dollar_Exchange FLOAT(20))"""




cursor.execute(sql)

# data2=[]


sql = "INSERT INTO GENERAL_INFORMATION(DATE, \
      JSE_ALL_SHARE,JSE_INDU,JSE_GOLD,RAND_US_Dollar_Exchange)\
      VALUES ('%s', '%f', '%f', '%f','%f')" % \
      (todays_date_str,float(jse_all_share),float(jse_indutop40),float(jse_gold),float(jse_zar_usd))
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
