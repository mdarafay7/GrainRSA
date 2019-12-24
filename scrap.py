#!/usr/bin/python

import bs4 as bs
import urllib.request
import csv
import pymysql
import re

source = urllib.request.urlopen('https://www.proteinresearch.net/index.php?page=expanded-price-averages-graph').read()
data=[['Date|Cape Town Harbour|Durban Harbour|Rand/US Dollar Exchange']]
soup = bs.BeautifulSoup(source,'html.parser')
table=soup.find("table")
table_body = table.find('tbody')
rows = table_body.find_all('tr')
string=''
db = pymysql.connect(host="localhost",user="root",password="test123",db="TESTDB" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS SOYBEAN");
sql = """CREATE TABLE SOYBEAN (
   DATE  VARCHAR(20) NOT NULL,
   CAPE_TOWN_HARBOUR  VARCHAR(20),
   DURBAN_HARBOUR VARCHAR(20),
   RAND_US_Dollar_Exchange VARCHAR(20))"""

cursor.execute(sql)

data2=[]



for row in rows:
    cols=row.find_all('td')
    string=''
    for col in cols:
        add=col.get_text()
        data2.append(add)
        print(add)
        string=string+add+'|'

    sql = "INSERT INTO SOYBEAN(DATE, \
       CAPE_TOWN_HARBOUR,DURBAN_HARBOUR,RAND_US_Dollar_Exchange)\
       VALUES ('%s', '%s', '%s', '%s')" % \
       (data2[0],data2[1],data2[2],data2[3])
    data2.clear()

    try:
       cursor.execute(sql)
       db.commit()
    except:
       db.rollback()


    data.append(string)

with open('data.csv', 'w+') as writeFile:
    writer = csv.writer(writeFile)
    for word in data:
        writer.writerow([word])

writeFile.close()

db.close()
