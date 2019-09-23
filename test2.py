import urllib.request
import bs4 as bs
import os
from datetime import date
import xlrd
from xlrd import open_workbook
import xlutils.copy
import xlwt
import pymysql
import sys
import re
import requests
import automata as auto
import time
import random

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}


db = pymysql.connect(host="localhost",user="root",password="Test123$",db="TESTDB" )
today = date.today()
#("Today's date:", today)
#()
today_str=today.strftime('%m/%d/%Y')

todays_month=today_str[0:2]
#(todays_month)
todays_day=today_str[3:5]
#(todays_day)

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS SAFEX_INFORMATION");
sql = """CREATE TABLE SAFEX_INFORMATION (
    DATE DATE NOT NULL,
    ID  CHAR(8) NOT NULL,
    COMMODITY VARCHAR(20) NOT NULL,
    SETTLEMENT FLOAT(7) NOT NULL,
    HIGH FLOAT(7) NOT NULL,
    LOW FLOAT(7) NOT NULL,
    VOL INT(4) NOT NULL,
    OPEN_INT FLOAT(8)
    )"""

cursor.execute(sql)

inBook = open_workbook('/home/mohammed/Documents/pythonproj/scraping/SAFEX.xls',formatting_info=True)

outBook = xlutils.copy.copy(inBook)
sheetsCount=inBook.nsheets
for each in range(sheetsCount):
    sheet=inBook.sheet_by_index(each)
    print(sheet.name)

day_minus=int(todays_day)-1
line_count=0
for i in range(12,day_minus):
    (i)

day_range=[]
day_plus=int(todays_day)+1

for i in range(12,day_plus):
    print(i)
    response = requests.get('https://www.jse.co.za/downloadable-files?RequestNode=/Safex/agriculture.stats/2019')
    soup=bs.BeautifulSoup(response.text,'html.parser')
    test = soup.findAll(text = re.compile('AGR'+todays_month+str(i)+'.xls'))
    print('check')
    if test:
        day_range.append(i)


for i in day_range:
    if(i==18):
        time.sleep(25)
    time.sleep(1+random.randint(1,10))
    url = 'https://www.jse.co.za/_layouts/15/DownloadHandler.ashx?FileName=/Safex/agriculture.stats/2019/AGR'+todays_month+str(i)+'.xls'
    print('getting')
    print(i)
    urllib.request.urlretrieve(url, '/home/mohammed/Documents/pythonproj/scraping/'+todays_month+str(i)+'.xls')
    print('todays_month'+str(i)+'.xls')
    loc=('/home/mohammed/Documents/pythonproj/scraping/'+todays_month+str(i)+'.xls')
    print(i)
    SAFEX_CONTRACT=xlrd.open_workbook(loc)
    SAFEX_SHEET=SAFEX_CONTRACT.sheet_by_index(0)
    auto.Inputter(line_count,SAFEX_SHEET,outBook,db,inBook,i)
    # auto.WHITE_MAIZE(line_count,SAFEX_SHEET,outBook,db,inBook,i)
    # auto.YELLOW_MAIZE(line_count,SAFEX_SHEET,outBook,db,inBook,i)
    # auto.BREAD_MILLING_WHEAT(line_count,SAFEX_SHEET,outBook,db,inBook,i)
    # auto.SUNFLOWER_SEEDS(line_count,SAFEX_SHEET,outBook,db,inBook,i)
    line_count=line_count+1



outBook.save('/home/mohammed/Documents/pythonproj/scraping/SAFEX2.xls')
