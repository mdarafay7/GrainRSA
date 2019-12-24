import bs4 as bs
import urllib.request
import csv
import pymysql
import re
import requests
from datetime import date
import automata as auto

def jse_DB():
    db = pymysql.connect(host="localhost",user="root",password="test123",db="TESTDB" )
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS GENERAL_INFORMATION");
    sql = """CREATE TABLE GENERAL_INFORMATION (
        DATE  VARCHAR(20) NOT NULL,
        JSE_ALL_SHARE FLOAT(20),
        JSE_INDU FLOAT(20),
        JSE_GOLD FLOAT(20),
        ZAR_USD FLOAT(20),
        GOLD FLOAT(20),
        ZAR_EUR FLOAT(20),
        ZAR_GBP FLOAT(20),
        USD_JPY FLOAT(20),
        BRENT_OIL FLOAT(20)
        )"""
    cursor.execute(sql)
