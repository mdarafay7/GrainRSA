import urllib.request
import bs4 as bs
import os
import datetime
from datetime import date
import xlrd
from xlrd import open_workbook
import xlutils.copy
import xlwt
import pymysql
import sys
import re
import requests



def float_conv(value):
    try:
        value="{:.2f}".format((float)(value))
        return value
    except:
        a=1



def Inputter(line_count,SAFEX_SHEET,outBook,db,inBook,add):
    for i in range(0,300):
        try:
            info=SAFEX_SHEET.row_values(i)
            WHITE_MAIZE_TRANSITSEPTEMBER19=[]
            WHITE_MAIZE_TRANSITOCTOBER19=[]
            WHITE_MAIZE_TRANSITDECEMBER19=[]
            WHITE_MAIZE_TRANSITMARCH20=[]
            WHITE_MAIZE_TRANSITMAY20=[]
            WHITE_MAIZE_TRANSITJULY20=[]
            WHITE_MAIZE_TRANSITSEPTEMBER20=[]
            WHITE_MAIZE_TRANSITDECEMBER20=[]
            #print(info)
            today = date.today()
            today_str=today.strftime('%m/%d/%Y')
            todays_month=today_str[0:2]
            today_str='2019-'+todays_month+'-'+str(add)
            if(info[0]=='WHITE MAIZE FUTURE'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(0).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(0).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    print(today_str)
                    print(info2)
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'WM',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='YELLOW MAIZE FUTURE'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(2).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(2).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    print(today_str)
                    print(info2)
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'YM',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='BREAD MILLING WHEAT'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(3).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(3).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'BMW',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SUNFLOWER SEEDS FUTURE'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SUN',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SOYA FUTURE'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(5).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(5).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SOYA',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SOYBEAN CONTRACT'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SOYBEAN',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='BREANT CRUDE OIL FUTURE'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'CRUDE',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),'*') #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='COPPER'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    print(today_str)
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'COPPER',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='CORN CONTRACT'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'CORN',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='DIESEL EUROPEAN GASOIL'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'DIESEL',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='GOLD'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'GOLD',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='HARD RED WINTER WHEAT FUTURES'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'HRW WHEAT',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SOYBEAN MEAL CONTRACT'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SOYBEAN MEAL',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='MINI SWEET SORGUM FUTURES'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SORGUM',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SOYBEAN OIL CONTRACT'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SOYBEAN OIL',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='PALLADIUM'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'PALLADIUM',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='PLATINUM'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'PLATINUM',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='BRENT CRUDE OIL QUANTO'):
                    for i2 in range(0,20):
                        info2=SAFEX_SHEET.row_values(i+i2+1)
                        try:
                            stringz=float(info2[0])
                        except ValueError:
                            break
                        pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                        month=pred_date.strftime("%B")
                        the_year=str(pred_date.year)
                        q=1
                        x=1
                        y=1
                        for value in info2[4:10]:
                            if q==2:
                                q=q+1
                            elif q>2:
                                if y==1 or y==2 or y==3:
                                    value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                            else:
                                value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                        cursor=db.cursor()
                        sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                            SETTLEMENT,HIGH,LOW,VOL)\
                            VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                           (today_str,'SAW'+month[0:3]+the_year[2:4],'CRUDE QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()

            elif(info[0]=='COFFEE QUANTO'):
                    for i2 in range(0,20):
                        info2=SAFEX_SHEET.row_values(i+i2+1)
                        try:
                            stringz=float(info2[0])
                        except ValueError:
                            break
                        pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                        month=pred_date.strftime("%B")
                        the_year=str(pred_date.year)
                        q=1
                        x=1
                        y=1
                        for value in info2[4:10]:
                            if q==2:
                                q=q+1
                            elif q>2:
                                if y==1 or y==2 or y==3:
                                    value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                            else:
                                value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                        cursor=db.cursor()
                        sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                            SETTLEMENT,HIGH,LOW,VOL)\
                            VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                           (today_str,'SAW'+month[0:3]+the_year[2:4],'COFFEE QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()

            elif(info[0]=='COPPER QUANTO'):
                    for i2 in range(0,20):
                        info2=SAFEX_SHEET.row_values(i+i2+1)
                        try:
                            stringz=float(info2[0])
                        except ValueError:
                            break
                        pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                        month=pred_date.strftime("%B")
                        the_year=str(pred_date.year)
                        q=1
                        x=1
                        y=1
                        for value in info2[4:10]:
                            if q==2:
                                q=q+1
                            elif q>2:
                                if y==1 or y==2 or y==3:
                                    value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                            else:
                                value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                        cursor=db.cursor()
                        sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                            SETTLEMENT,HIGH,LOW,VOL)\
                            VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                           (today_str,'SAW'+month[0:3]+the_year[2:4],'COPPER QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()


            elif(info[0]=='CORN QUANTO'):
                    for i2 in range(0,20):
                        info2=SAFEX_SHEET.row_values(i+i2+1)
                        try:
                            stringz=float(info2[0])
                        except ValueError:
                            break
                        pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                        month=pred_date.strftime("%B")
                        the_year=str(pred_date.year)
                        q=1
                        x=1
                        y=1
                        for value in info2[4:10]:
                            if q==2:
                                q=q+1
                            elif q>2:
                                if y==1 or y==2 or y==3:
                                    value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                            else:
                                value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                        cursor=db.cursor()
                        sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                            SETTLEMENT,HIGH,LOW,VOL)\
                            VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                           (today_str,'SAW'+month[0:3]+the_year[2:4],'CORN QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()

            elif(info[0]=='GOLD QUANTO'):
                    for i2 in range(0,20):
                        info2=SAFEX_SHEET.row_values(i+i2+1)
                        try:
                            stringz=float(info2[0])
                        except ValueError:
                            break
                        pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                        month=pred_date.strftime("%B")
                        the_year=str(pred_date.year)
                        q=1
                        x=1
                        y=1
                        for value in info2[4:10]:
                            if q==2:
                                q=q+1
                            elif q>2:
                                if y==1 or y==2 or y==3:
                                    value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                            else:
                                value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                        cursor=db.cursor()
                        sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                            SETTLEMENT,HIGH,LOW,VOL)\
                            VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                           (today_str,'SAW'+month[0:3]+the_year[2:4],'GOLD QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()

            elif(info[0]=='PALLADIUM QUANTO'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'PALLADIUM QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='PLATINUM QUANTO'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'PLATINUM QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SOYBEAN QUANTO'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SOYBEAN QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SILVER QUANTO'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SILVER QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SUGAR #11 QUANTO'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SUGAR #11 QUANTO',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SOFT RED WHEAT FUTURES'):
                for i2 in range(0,20):
                    info2=SAFEX_SHEET.row_values(i+i2+1)
                    try:
                        stringz=float(info2[0])
                    except ValueError:
                        break
                    pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                    month=pred_date.strftime("%B")
                    the_year=str(pred_date.year)
                    q=1
                    x=1
                    y=1
                    for value in info2[4:10]:
                        if q==2:
                            q=q+1
                        elif q>2:
                            if y==1 or y==2 or y==3:
                                value=float_conv(value)
                            outBook.get_sheet(3).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                        else:
                            value=float_conv(value)
                            outBook.get_sheet(3).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                            info2.append(value)
                            q=i+1
                            x=x+1
                            y=y+1
                    cursor=db.cursor()
                    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
                        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
                       (today_str,'SAW'+month[0:3]+the_year[2:4],'SOFT READ WHEAT',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8]),float(info2[9])) #continue from here create the right format before WM and have a proper string
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            elif(info[0]=='SILVER'):
                    for i2 in range(0,20):
                        info2=SAFEX_SHEET.row_values(i+i2+1)
                        try:
                            stringz=float(info2[0])
                        except ValueError:
                            break
                        pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                        month=pred_date.strftime("%B")
                        the_year=str(pred_date.year)
                        q=1
                        x=1
                        y=1
                        for value in info2[4:10]:
                            if q==2:
                                q=q+1
                            elif q>2:
                                if y==1 or y==2 or y==3:
                                    value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                            else:
                                value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                        cursor=db.cursor()
                        sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                            SETTLEMENT,HIGH,LOW,VOL)\
                            VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                           (today_str,'SAW'+month[0:3]+the_year[2:4],'SILVER',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()

            elif(info[0]=='CRUDE OIL'):
                    for i2 in range(0,20):
                        info2=SAFEX_SHEET.row_values(i+i2+1)
                        try:
                            stringz=float(info2[0])
                        except ValueError:
                            break
                        pred_date = datetime.datetime(*xlrd.xldate_as_tuple(info2[0],inBook.datemode))
                        month=pred_date.strftime("%B")
                        the_year=str(pred_date.year)
                        q=1
                        x=1
                        y=1
                        for value in info2[4:10]:
                            if q==2:
                                q=q+1
                            elif q>2:
                                if y==1 or y==2 or y==3:
                                    value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                            else:
                                value=float_conv(value)
                                outBook.get_sheet(4).write(240+add,x,value, xlwt.easyxf("align: horiz right"))
                                info2.append(value)
                                q=i+1
                                x=x+1
                                y=y+1
                        cursor=db.cursor()
                        sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
                            SETTLEMENT,HIGH,LOW,VOL)\
                            VALUES ('%s','%s','%s','%f','%f', '%f','%f')" % \
                           (today_str,'SAW'+month[0:3]+the_year[2:4],'CRUDE OIL',float(info2[3]),float(info2[6]),float(info2[7]),float(info2[8])) #continue from here create the right format before WM and have a proper string
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()







        except IndexError:
            break
            #print ("Error: can\'t find file or read data")





































def WHITE_MAIZE(p,SAFEX_SHEET,outBook,db,inBook,add):
    WHITE_MAIZE_SEPTEMBER19=SAFEX_SHEET.row_values(6)
    WHITE_MAIZE_OCTOBER19=SAFEX_SHEET.row_values(7)
    WHITE_MAIZE_DECEMBER19=SAFEX_SHEET.row_values(8)
    WHITE_MAIZE_MARCH20=SAFEX_SHEET.row_values(9)
    WHITE_MAIZE_MAY20=SAFEX_SHEET.row_values(10)
    WHITE_MAIZE_JULY20=SAFEX_SHEET.row_values(11)
    WHITE_MAIZE_SEPTEMBER20=SAFEX_SHEET.row_values(12)
    WHITE_MAIZE_DECEMBER20=SAFEX_SHEET.row_values(13)
    today = date.today()
    today_str=today.strftime('%m/%d/%Y')
    todays_month=today_str[0:2]
    today_str='2019-'+todays_month+'-'+str(add)
    i=1
    x=1
    y=1
    WHITE_MAIZE_TRANSITSEPTEMBER19=[]
    WHITE_MAIZE_TRANSITOCTOBER19=[]
    WHITE_MAIZE_TRANSITDECEMBER19=[]
    WHITE_MAIZE_TRANSITMARCH20=[]
    WHITE_MAIZE_TRANSITMAY20=[]
    WHITE_MAIZE_TRANSITJULY20=[]
    WHITE_MAIZE_TRANSITSEPTEMBER20=[]
    WHITE_MAIZE_TRANSITDECEMBER20=[]

    for value in WHITE_MAIZE_SEPTEMBER19[4:10]:
        WHITE_MAIZE_TRANSITSEPTEMBER19.append(WHITE_MAIZE_SEPTEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWSep19','WM',float(WHITE_MAIZE_TRANSITSEPTEMBER19[1]),float(WHITE_MAIZE_TRANSITSEPTEMBER19[4]),float(WHITE_MAIZE_TRANSITSEPTEMBER19[6]),float(WHITE_MAIZE_TRANSITSEPTEMBER19[8]),float(WHITE_MAIZE_TRANSITSEPTEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


    i=1
    x=6
    y=1
    for value in WHITE_MAIZE_OCTOBER19[4:10]:
        WHITE_MAIZE_TRANSITOCTOBER19.append(WHITE_MAIZE_OCTOBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITOCTOBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITOCTOBER19.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(WHITE_MAIZE_TRANSITOCTOBER19)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWOct19','WM',float(WHITE_MAIZE_TRANSITOCTOBER19[1]),float(WHITE_MAIZE_TRANSITOCTOBER19[4]),float(WHITE_MAIZE_TRANSITOCTOBER19[6]),float(WHITE_MAIZE_TRANSITOCTOBER19[8]),float(WHITE_MAIZE_TRANSITOCTOBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


    i=1
    x=11
    y=1
    for value in WHITE_MAIZE_DECEMBER19[4:10]:
        WHITE_MAIZE_TRANSITDECEMBER19.append(WHITE_MAIZE_DECEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWDec19','WM',float(WHITE_MAIZE_TRANSITDECEMBER19[1]),float(WHITE_MAIZE_TRANSITDECEMBER19[4]),float(WHITE_MAIZE_TRANSITDECEMBER19[6]),float(WHITE_MAIZE_TRANSITDECEMBER19[8]),float(WHITE_MAIZE_TRANSITDECEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


    i=1
    x=16
    y=1
    for value in WHITE_MAIZE_MARCH20[4:10]:
        WHITE_MAIZE_TRANSITMARCH20.append(WHITE_MAIZE_MARCH20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMar20','WM',float(WHITE_MAIZE_TRANSITMARCH20[1]),float(WHITE_MAIZE_TRANSITMARCH20[4]),float(WHITE_MAIZE_TRANSITMARCH20[6]),float(WHITE_MAIZE_TRANSITMARCH20[8]),float(WHITE_MAIZE_TRANSITMARCH20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=21
    y=1
    for value in WHITE_MAIZE_MAY20[4:10]:
        WHITE_MAIZE_TRANSITMAY20.append(WHITE_MAIZE_MAY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMay20','WM',float(WHITE_MAIZE_TRANSITMAY20[1]),float(WHITE_MAIZE_TRANSITMAY20[4]),float(WHITE_MAIZE_TRANSITMAY20[6]),float(WHITE_MAIZE_TRANSITMAY20[8]),float(WHITE_MAIZE_TRANSITMAY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


    i=1
    x=26
    y=1
    for value in WHITE_MAIZE_JULY20[4:10]:
        WHITE_MAIZE_TRANSITJULY20.append(WHITE_MAIZE_JULY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWJul20','WM',float(WHITE_MAIZE_TRANSITJULY20[1]),float(WHITE_MAIZE_TRANSITJULY20[4]),float(WHITE_MAIZE_TRANSITJULY20[6]),float(WHITE_MAIZE_TRANSITJULY20[8]),float(WHITE_MAIZE_TRANSITJULY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    i=1
    x=31
    y=1
    for value in WHITE_MAIZE_SEPTEMBER20[4:10]:
        WHITE_MAIZE_TRANSITSEPTEMBER20.append(WHITE_MAIZE_SEPTEMBER20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITSEPTEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITSEPTEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWSep20','WM',float(WHITE_MAIZE_TRANSITSEPTEMBER20[1]),float(WHITE_MAIZE_TRANSITSEPTEMBER20[4]),float(WHITE_MAIZE_TRANSITSEPTEMBER20[6]),float(WHITE_MAIZE_TRANSITSEPTEMBER20[8]),float(WHITE_MAIZE_TRANSITSEPTEMBER20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=36
    y=1
    for value in WHITE_MAIZE_DECEMBER20[4:10]:
        WHITE_MAIZE_TRANSITDECEMBER20.append(WHITE_MAIZE_DECEMBER20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITDECEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(0).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            WHITE_MAIZE_TRANSITDECEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1

    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWDec20','WM',float(WHITE_MAIZE_TRANSITDECEMBER20[1]),float(WHITE_MAIZE_TRANSITDECEMBER20[4]),float(WHITE_MAIZE_TRANSITDECEMBER20[6]),float(WHITE_MAIZE_TRANSITDECEMBER20[8]),float(WHITE_MAIZE_TRANSITDECEMBER20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()





def YELLOW_MAIZE(p,SAFEX_SHEET,outBook,db,inBook,add):
    YELLOW_MAIZE_SEPTEMBER19=SAFEX_SHEET.row_values(15)
    YELLOW_MAIZE_OCTOBER19=SAFEX_SHEET.row_values(16)
    YELLOW_MAIZE_DECEMBER19=SAFEX_SHEET.row_values(17)
    YELLOW_MAIZE_MARCH20=SAFEX_SHEET.row_values(18)
    YELLOW_MAIZE_MAY20=SAFEX_SHEET.row_values(19)
    YELLOW_MAIZE_JULY20=SAFEX_SHEET.row_values(20)
    YELLOW_MAIZE_SEPTEMBER20=SAFEX_SHEET.row_values(21)
    YELLOW_MAIZE_DECEMBER20=SAFEX_SHEET.row_values(22)

    YELLOW_MAIZE_TRANSITSEPTEMBER19=[]
    YELLOW_MAIZE_TRANSITOCTOBER19=[]
    YELLOW_MAIZE_TRANSITDECEMBER19=[]
    YELLOW_MAIZE_TRANSITMARCH20=[]
    YELLOW_MAIZE_TRANSITMAY20=[]
    YELLOW_MAIZE_TRANSITJULY20=[]
    YELLOW_MAIZE_TRANSITSEPTEMBER20=[]
    YELLOW_MAIZE_TRANSITDECEMBER20=[]
    YELLOW_MAIZE_TRANSITNOVEMBER19=[]

    today = date.today()
    today_str=today.strftime('%m/%d/%Y')
    todays_month=today_str[0:2]
    today_str='2019-'+todays_month+'-'+str(add)



    i=1
    x=1
    y=1
    for value in YELLOW_MAIZE_SEPTEMBER19[4:10]:
        YELLOW_MAIZE_TRANSITSEPTEMBER19.append(YELLOW_MAIZE_SEPTEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWSep19','YM',float(YELLOW_MAIZE_TRANSITSEPTEMBER19[1]),float(YELLOW_MAIZE_TRANSITSEPTEMBER19[4]),float(YELLOW_MAIZE_TRANSITSEPTEMBER19[6]),float(YELLOW_MAIZE_TRANSITSEPTEMBER19[8]),float(YELLOW_MAIZE_TRANSITSEPTEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=6
    y=1
    for value in YELLOW_MAIZE_OCTOBER19[4:10]:
        YELLOW_MAIZE_TRANSITOCTOBER19.append(YELLOW_MAIZE_OCTOBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITOCTOBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITOCTOBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWOct19','YM',float(YELLOW_MAIZE_TRANSITOCTOBER19[1]),float(YELLOW_MAIZE_TRANSITOCTOBER19[4]),float(YELLOW_MAIZE_TRANSITOCTOBER19[6]),float(YELLOW_MAIZE_TRANSITOCTOBER19[8]),float(YELLOW_MAIZE_TRANSITOCTOBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


    i=1
    x=11
    y=1
    for value in YELLOW_MAIZE_DECEMBER19[4:10]:
        YELLOW_MAIZE_TRANSITDECEMBER19.append(YELLOW_MAIZE_DECEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWDec19','YM',float(YELLOW_MAIZE_TRANSITDECEMBER19[1]),float(YELLOW_MAIZE_TRANSITDECEMBER19[4]),float(YELLOW_MAIZE_TRANSITDECEMBER19[6]),float(YELLOW_MAIZE_TRANSITDECEMBER19[8]),float(YELLOW_MAIZE_TRANSITDECEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=16
    y=1
    for value in YELLOW_MAIZE_MARCH20[4:10]:
        YELLOW_MAIZE_TRANSITMARCH20.append(YELLOW_MAIZE_MARCH20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMar20','YM',float(YELLOW_MAIZE_TRANSITMARCH20[1]),float(YELLOW_MAIZE_TRANSITMARCH20[4]),float(YELLOW_MAIZE_TRANSITMARCH20[6]),float(YELLOW_MAIZE_TRANSITMARCH20[8]),float(YELLOW_MAIZE_TRANSITMARCH20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    i=1
    x=21
    y=1
    for value in YELLOW_MAIZE_MAY20[4:10]:
        YELLOW_MAIZE_TRANSITMAY20.append(YELLOW_MAIZE_MAY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMay20','YM',float(YELLOW_MAIZE_TRANSITMAY20[1]),float(YELLOW_MAIZE_TRANSITMAY20[4]),float(YELLOW_MAIZE_TRANSITMAY20[6]),float(YELLOW_MAIZE_TRANSITMAY20[8]),float(YELLOW_MAIZE_TRANSITMAY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=26
    y=1
    for value in YELLOW_MAIZE_JULY20[4:10]:
        YELLOW_MAIZE_TRANSITJULY20.append(YELLOW_MAIZE_JULY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWJul20','YM',float(YELLOW_MAIZE_TRANSITJULY20[1]),float(YELLOW_MAIZE_TRANSITJULY20[4]),float(YELLOW_MAIZE_TRANSITJULY20[6]),float(YELLOW_MAIZE_TRANSITJULY20[8]),float(YELLOW_MAIZE_TRANSITJULY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=31
    y=1
    for value in YELLOW_MAIZE_SEPTEMBER20[4:10]:
        YELLOW_MAIZE_TRANSITSEPTEMBER20.append(YELLOW_MAIZE_SEPTEMBER20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITSEPTEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITSEPTEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWSep20','YM',float(YELLOW_MAIZE_TRANSITSEPTEMBER20[1]),float(YELLOW_MAIZE_TRANSITSEPTEMBER20[4]),float(YELLOW_MAIZE_TRANSITSEPTEMBER20[6]),float(YELLOW_MAIZE_TRANSITSEPTEMBER20[8]),float(YELLOW_MAIZE_TRANSITSEPTEMBER20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=46
    y=1
    for value in YELLOW_MAIZE_DECEMBER20[4:10]:
        YELLOW_MAIZE_TRANSITDECEMBER20.append(YELLOW_MAIZE_DECEMBER20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITDECEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            YELLOW_MAIZE_TRANSITDECEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    #print(YELLOW_MAIZE_TRANSITSEPTEMBER20)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWDec20','YM',float(YELLOW_MAIZE_TRANSITDECEMBER20[1]),float(YELLOW_MAIZE_TRANSITDECEMBER20[4]),float(YELLOW_MAIZE_TRANSITDECEMBER20[6]),float(YELLOW_MAIZE_TRANSITDECEMBER20[8]),float(YELLOW_MAIZE_TRANSITDECEMBER20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

def BREAD_MILLING_WHEAT(p,SAFEX_SHEET,outBook,db,inBook,add):
    BREAD_MILLING_WHEAT_SEPTEMBER19=SAFEX_SHEET.row_values(24)
    BREAD_MILLING_WHEAT_DECEMBER19=SAFEX_SHEET.row_values(25)
    BREAD_MILLING_WHEAT_MARCH20=SAFEX_SHEET.row_values(26)
    BREAD_MILLING_WHEAT_MAY20=SAFEX_SHEET.row_values(27)
    BREAD_MILLING_WHEAT_JULY20=SAFEX_SHEET.row_values(28)

    BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19=[]
    BREAD_MILLING_WHEAT_TRANSITDECEMBER19=[]
    BREAD_MILLING_WHEAT_TRANSITMARCH20=[]
    BREAD_MILLING_WHEAT_TRANSITMAY20=[]
    BREAD_MILLING_WHEAT_TRANSITJULY20=[]

    today = date.today()
    today_str=today.strftime('%m/%d/%Y')
    todays_month=today_str[0:2]
    today_str='2019-'+todays_month+'-'+str(add)

    i=1
    x=1
    y=1
    for value in BREAD_MILLING_WHEAT_SEPTEMBER19[4:10]:
        BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19.append(BREAD_MILLING_WHEAT_SEPTEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWSep19','BMW',float(BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19[1]),float(BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19[4]),float(BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19[6]),float(BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19[8]),float(BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=6
    y=1
    for value in BREAD_MILLING_WHEAT_DECEMBER19[4:10]:
        BREAD_MILLING_WHEAT_TRANSITDECEMBER19.append(BREAD_MILLING_WHEAT_DECEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWDec19','BMW',float(BREAD_MILLING_WHEAT_TRANSITDECEMBER19[1]),float(BREAD_MILLING_WHEAT_TRANSITDECEMBER19[4]),float(BREAD_MILLING_WHEAT_TRANSITDECEMBER19[6]),float(BREAD_MILLING_WHEAT_TRANSITDECEMBER19[8]),float(BREAD_MILLING_WHEAT_TRANSITDECEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=11
    y=1
    for value in BREAD_MILLING_WHEAT_MARCH20[4:10]:
        BREAD_MILLING_WHEAT_TRANSITMARCH20.append(BREAD_MILLING_WHEAT_MARCH20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMar20','BMW',float(BREAD_MILLING_WHEAT_TRANSITMARCH20[1]),float(BREAD_MILLING_WHEAT_TRANSITMARCH20[4]),float(BREAD_MILLING_WHEAT_TRANSITMARCH20[6]),float(BREAD_MILLING_WHEAT_TRANSITMARCH20[8]),float(BREAD_MILLING_WHEAT_TRANSITMARCH20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=16
    y=1
    for value in BREAD_MILLING_WHEAT_MAY20[4:10]:
        BREAD_MILLING_WHEAT_TRANSITMAY20.append(BREAD_MILLING_WHEAT_MAY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMay20','BMW',float(BREAD_MILLING_WHEAT_TRANSITMAY20[1]),float(BREAD_MILLING_WHEAT_TRANSITMAY20[4]),float(BREAD_MILLING_WHEAT_TRANSITMAY20[6]),float(BREAD_MILLING_WHEAT_TRANSITMAY20[8]),float(BREAD_MILLING_WHEAT_TRANSITMAY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=21
    y=1
    for value in BREAD_MILLING_WHEAT_JULY20[4:10]:
        BREAD_MILLING_WHEAT_TRANSITJULY20.append(BREAD_MILLING_WHEAT_JULY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(3).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            BREAD_MILLING_WHEAT_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    print(BREAD_MILLING_WHEAT_TRANSITSEPTEMBER19)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWJul20','BMW',float(BREAD_MILLING_WHEAT_TRANSITJULY20[1]),float(BREAD_MILLING_WHEAT_TRANSITJULY20[4]),float(BREAD_MILLING_WHEAT_TRANSITJULY20[6]),float(BREAD_MILLING_WHEAT_TRANSITJULY20[8]),float(BREAD_MILLING_WHEAT_TRANSITJULY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()




def SUNFLOWER_SEEDS(p,SAFEX_SHEET,outBook,db,inBook,add):
    SUNFLOWER_SEEDS_SEPTEMBER19=SAFEX_SHEET.row_values(30)
    SUNFLOWER_SEEDS_DECEMBER19=SAFEX_SHEET.row_values(31)
    SUNFLOWER_SEEDS_MARCH20=SAFEX_SHEET.row_values(32)
    SUNFLOWER_SEEDS_MAY20=SAFEX_SHEET.row_values(33)
    SUNFLOWER_SEEDS_JULY20=SAFEX_SHEET.row_values(34)
    SUNFLOWER_SEEDS_DECEMBER20=SAFEX_SHEET.row_values(35)

    SUNFLOWER_SEEDS_TRANSITSEPTEMBER19=[]
    SUNFLOWER_SEEDS_TRANSITDECEMBER19=[]
    SUNFLOWER_SEEDS_TRANSITMARCH20=[]
    SUNFLOWER_SEEDS_TRANSITMAY20=[]
    SUNFLOWER_SEEDS_TRANSITJULY20=[]
    SUNFLOWER_SEEDS_TRANSITDECEMBER20=[]

    today = date.today()
    today_str=today.strftime('%m/%d/%Y')
    todays_month=today_str[0:2]
    today_str='2019-'+todays_month+'-'+str(add)



    i=1
    x=1
    y=1
    for value in SUNFLOWER_SEEDS_SEPTEMBER19[4:10]:
        SUNFLOWER_SEEDS_TRANSITSEPTEMBER19.append(SUNFLOWER_SEEDS_SEPTEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITSEPTEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWSep19','SUN',float(SUNFLOWER_SEEDS_TRANSITSEPTEMBER19[1]),float(SUNFLOWER_SEEDS_TRANSITSEPTEMBER19[4]),float(SUNFLOWER_SEEDS_TRANSITSEPTEMBER19[6]),float(SUNFLOWER_SEEDS_TRANSITSEPTEMBER19[8]),float(SUNFLOWER_SEEDS_TRANSITSEPTEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    i=1
    x=6
    y=1
    for value in SUNFLOWER_SEEDS_DECEMBER19[4:10]:
        SUNFLOWER_SEEDS_TRANSITDECEMBER19.append(SUNFLOWER_SEEDS_DECEMBER19[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITDECEMBER19.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWDec19','SUN',float(SUNFLOWER_SEEDS_TRANSITDECEMBER19[1]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER19[4]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER19[6]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER19[8]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER19[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=11
    y=1
    for value in SUNFLOWER_SEEDS_MARCH20[4:10]:
        SUNFLOWER_SEEDS_TRANSITMARCH20.append(SUNFLOWER_SEEDS_MARCH20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITMARCH20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMar20','SUN',float(SUNFLOWER_SEEDS_TRANSITMARCH20[1]),float(SUNFLOWER_SEEDS_TRANSITMARCH20[4]),float(SUNFLOWER_SEEDS_TRANSITMARCH20[6]),float(SUNFLOWER_SEEDS_TRANSITMARCH20[8]),float(SUNFLOWER_SEEDS_TRANSITMARCH20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=16
    y=1
    for value in SUNFLOWER_SEEDS_MAY20[4:10]:
        SUNFLOWER_SEEDS_TRANSITMAY20.append(SUNFLOWER_SEEDS_MAY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITMAY20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWMay20','SUN',float(SUNFLOWER_SEEDS_TRANSITMAY20[1]),float(SUNFLOWER_SEEDS_TRANSITMAY20[4]),float(SUNFLOWER_SEEDS_TRANSITMAY20[6]),float(SUNFLOWER_SEEDS_TRANSITMAY20[8]),float(SUNFLOWER_SEEDS_TRANSITMAY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=21
    y=1
    for value in SUNFLOWER_SEEDS_JULY20[4:10]:
        SUNFLOWER_SEEDS_TRANSITJULY20.append(SUNFLOWER_SEEDS_JULY20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITJULY20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWJul20','SUN',float(SUNFLOWER_SEEDS_TRANSITJULY20[1]),float(SUNFLOWER_SEEDS_TRANSITJULY20[4]),float(SUNFLOWER_SEEDS_TRANSITJULY20[6]),float(SUNFLOWER_SEEDS_TRANSITJULY20[8]),float(SUNFLOWER_SEEDS_TRANSITJULY20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    i=1
    x=26
    y=1
    for value in SUNFLOWER_SEEDS_DECEMBER20[4:10]:
        SUNFLOWER_SEEDS_TRANSITDECEMBER20.append(SUNFLOWER_SEEDS_DECEMBER20[0])
        if i==2:
            i=i+1
        elif i>2:
            if y==1 or y==2 or y==3:
                value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITDECEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
        else:
            value=float_conv(value)
            outBook.get_sheet(2).write(240+p,x,value, xlwt.easyxf("align: horiz right"))
            SUNFLOWER_SEEDS_TRANSITDECEMBER20.append(value)
            i=i+1
            x=x+1
            y=y+1
    cursor=db.cursor()
    print(today_str)
    sql = "INSERT INTO SAFEX_INFORMATION(DATE,ID,COMMODITY,\
        SETTLEMENT,HIGH,LOW,VOL,OPEN_INT)\
        VALUES ('%s','%s','%s','%f','%f', '%f','%f','%f')" % \
       (today_str,'SAWDec20','SUN',float(SUNFLOWER_SEEDS_TRANSITDECEMBER20[1]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER20[4]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER20[6]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER20[8]),float(SUNFLOWER_SEEDS_TRANSITDECEMBER20[10])) #continue from here create the right format before WM and have a proper string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

# SOYA_SEPTEMBER19=SAFEX_SHEET.row_values(38)
# SOYA_OCTOBER19=SAFEX_SHEET.row_values(39)
# SOYA_DECEMBER19=SAFEX_SHEET.row_values(40)
# SOYA_MARCH20=SAFEX_SHEET.row_values(41)
# SOYA_MAY20=SAFEX_SHEET.row_values(42)
# SOYA_SEPTEMBER20=SAFEX_SHEET.row_values(43)
#
# SOYBEAN_NOVEMBER19=SAFEX_SHEET.row_values(45)
# SOYBEAN_MARCH20=SAFEX_SHEET.row_values(46)
# SOYBEAN_MAY20=SAFEX_SHEET.row_values(47)
#
# CORN_CONTRACT_DECEMBER19=SAFEX_SHEET.row_values(55)
# CORN_CONTRACT_MARCH20=SAFEX_SHEET.row_values(56)
# CORN_CONTRACT_JULY20=SAFEX_SHEET.row_values(57)
# CORN_CONTRACT_SEPTEMBER20=SAFEX_SHEET.row_values(58)
#
# HRW_WHEAT_DECEMBER19=SAFEX_SHEET.row_values(55)
# HRW_WHEAT_MARCH20=SAFEX_SHEET.row_values(56)
#
# SORGUM_MARCH20=SAFEX_SHEET.row_values(72)
#
# SOYBEAN_OIL_DECEMBER19=SAFEX_SHEET.row_values(74)
