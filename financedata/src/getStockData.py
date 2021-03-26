
#!/bin/env python3
# Author  : freeman
# Date    : 2021.03.25
# Desc    : This software will export by default the past year STOCK price {high, low, open, close} 
#         : Financialmodelingprep doesnt have all the Class-C mutual fund types.
#         : yet, it is the only site with API listngs of Cryptocurrencies.
#         : 
# use     : python3 getStockData.py
# Version : 0.0.1
###################################################################


from datetime import datetime, timedelta
import warnings
import json
import sys
import os.path
from os import path
import socket

__NDAYS_AGO__ = 366

try:
    from requests.exceptions import HTTPError
    import requests
except ImportError as herr:
    print("Missing requests library")
    print("pip install --user requests")


try:
    import urllib3
except ImportError as err:
    warnings.warn('No Package named urllib3 was found. ', ImportWarning)
    print(err.__class__.__name__ + " : " + err.__cause__)
    sys.exit(1)


def testConn():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError as err:
        print("No Connection: " + err.errno)
    return False


def computeDate():
    # Sublimate the Date Magic
    date_list = []
    a = datetime.now()
    b = a - timedelta(days=__NDAYS_AGO__)
    today_date = str(str(a).split(' ')[0])
    days_ago = str(str(b).split(' ')[0])
    date_list.append(today_date)
    date_list.append(days_ago)
    return date_list


# default:  https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?from=2020-03-01&to=2021-03-01&apikey=demo
def retrieveStockTickerInfo(t, s, e):
    KEY = "YOUR_MODELING_PREDICTION_SITE_KEY"
    if KEY == "YOUR_MODELING_PREDICTION_SITE_KEY":
        print("You will need to setup and obtain an account before using this software")
        sys.exit(2)
    else:
        pass

    url = "https://financialmodelingprep.com/api/v3/historical-price-full/" + t.upper() + "?from=" + s + "&to=" + e + "&apikey=" + KEY

    try:
        r = requests.get(url=url)
        r.encoding = 'ISO-8859-1'
        r.raise_for_status()
        data = r.json()
    except HTTPError as err:
        print("Http Connection Error", err.response)
        sys.exit()

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def processFields():
    ds, tds, sopen, sclose, shigh, slow = {}, [], {}, {}, {}, {}
    tmp1, tmp2 = "", ""
    so, sc, sh, sl = {}, {}, {}, {}

    with open('data.json', 'r') as f:
        ds = json.load(f)

    # date:open, high, close, low
    tds = ds['historical']
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "open":
                tmp2 = "{:.2f}".format(v)
            sopen.update({tmp1:tmp2})
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "close":
                tmp2 = "{:.2f}".format(v)
            sclose.update({tmp1:tmp2})
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "high":
                tmp2 = "{:.2f}".format(v)
            shigh.update({tmp1:tmp2})
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "low":
                tmp2 = "{:.2f}".format(v)
            slow.update({tmp1:tmp2})
    
    # Apparently, one OPEN key:value is blank
    ek = [k for k, v in sopen.items() if not v]
    for k in ek:
        del sopen[k]

    # sorting
    tmp = sorted(sopen,reverse=True)
    for k in tmp:
        so.update({k:sopen[k]})
    # sorting
    tmp = sorted(sclose,reverse=True)
    for k in tmp:
        sc.update({k:sopen[k]})
    # sorting
    tmp = sorted(shigh,reverse=True)
    for k in tmp:
        sh.update({k:sopen[k]})
    # sorting
    tmp = sorted(slow,reverse=True)
    for k in tmp:
        sl.update({k:sopen[k]})

    # Most recent on top with title
    x1 = {"date":"open"}
    x2 = {"date":"close"}
    x3 = {"date":"high"}
    x4 = {"date":"low"}
    so = {**x1, **so}
    sc = {**x2, **sc}
    sh = {**x3, **sh}
    sl = {**x4, **sl}

    return so, sc, sh, sl


def processFieldsRev():
    ds, tds, sopen, sclose, shigh, slow = {}, [], {}, {}, {}, {}
    tmp1, tmp2 = "", ""
    so, sc, sh, sl = {}, {}, {}, {}

    with open('data.json', 'r') as f:
        ds = json.load(f)

    # date:open, high, close, low
    tds = ds['historical']
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "open":
                tmp2 = "{:.2f}".format(v)
            sopen.update({tmp1:tmp2})
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "close":
                tmp2 = "{:.2f}".format(v)
            sclose.update({tmp1:tmp2})
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "high":
                tmp2 = "{:.2f}".format(v)
            shigh.update({tmp1:tmp2})
    for i in tds:
        for k, v in i.items():
            if str(k).strip().lower() == "date":
                tmp1 = v
            if str(k).strip().lower() == "low":
                tmp2 = "{:.2f}".format(v)
            slow.update({tmp1:tmp2})
    
    # Apparently, one OPEN key:value is blank
    ek = [k for k, v in sopen.items() if not v]
    for k in ek:
        del sopen[k]

    # sorting
    tmp = sorted(sopen)
    for k in tmp:
        so.update({k:sopen[k]})
    # sorting
    tmp = sorted(sclose)
    for k in tmp:
        sc.update({k:sopen[k]})
    # sorting
    tmp = sorted(shigh)
    for k in tmp:
        sh.update({k:sopen[k]})
    # sorting
    tmp = sorted(slow)
    for k in tmp:
        sl.update({k:sopen[k]})

    # Most recent on bottom  with title
    x1 = {"date":"open"}
    x2 = {"date":"close"}
    x3 = {"date":"high"}
    x4 = {"date":"low"}
    so = {**x1, **so}
    sc = {**x2, **sc}
    sh = {**x3, **sh}
    sl = {**x4, **sl}

    return so, sc, sh, sl


def writeToDisk(t, so, sc, sh, sl):

    fname1 = t + "_open_data.csv"
    fname2 = t + "_close_data.csv"
    fname3 = t + "_high_data.csv"
    fname4 = t + "_low_data.csv"
    tmp = ""
    with open(fname1, "w", encoding='utf-8' ) as f: 
        for k, v in so.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""
    with open(fname2, "w", encoding='utf-8' ) as f: 
        for k, v in sc.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""
    with open(fname3, "w", encoding='utf-8' ) as f: 
        for k, v in sh.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""
    with open(fname4, "w", encoding='utf-8' ) as f: 
        for k, v in sl.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""


def writeToDiskRev(t, so, sc, sh, sl):    

    fname1 = t + "_open_data_rev.csv"
    fname2 = t + "_close_data_rev.csv"
    fname3 = t + "_high_data_rev.csv"
    fname4 = t + "_low_data_rev.csv"
    tmp = ""

    with open(fname1, "w", encoding='utf-8' ) as f: 
        for k, v in so.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""
    with open(fname2, "w", encoding='utf-8' ) as f: 
        for k, v in sc.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""
    with open(fname3, "w", encoding='utf-8' ) as f: 
        for k, v in sh.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""
    with open(fname4, "w", encoding='utf-8' ) as f: 
        for k, v in sl.items():
            tmp = str(k)+','+str(v)+"\n"
            f.write(tmp)
            tmp = ""


def main():

    ticker, start_date, end_date = "", "", ""

    ticker = input("Enter in a stock Ticker >> ").strip()
    start_date = input("Enter in a Start date in form yyyy-mm-dd or blank >> ").strip()
    end_date =   input("Enter in a End date in form yyyy-mm-dd or blank   >> ").strip()

    # man, parsing JSON data is giving me major heart burn
    # brain wasnt functional when i wanted to work on this part below
    if testConn() == True:
        if ticker.isspace() or ticker == "" or ticker == None:
            print("Ticker Field is Blank, where it must have a single Stock value !")
            sys.exit(1)
        else:
            if ( start_date.isspace() or start_date == "" or start_date == None ) and ( end_date.isspace() or end_date == "" or end_date == None ):
                start_date = str(computeDate()[0]).strip()
                end_date = str(computeDate()[1]).strip()
                retrieveStockTickerInfo(ticker, end_date, start_date)
                a,b,c,d = processFields()
                writeToDisk(ticker, a,b,c, d)
                a,b,c,d = processFieldsRev()
                writeToDiskRev(ticker, a,b,c,d)
            elif ( not start_date.isspace() or not start_date == "" or not start_date == None) and  ( not end_date.isspace() or not end_date == "" or not end_date == None):
                retrieveStockTickerInfo(ticker, start_date, end_date)
                a,b,c,d = processFields()
                writeToDisk(ticker, a,b,c, d)
                a,b,c,d = processFieldsRev()
                writeToDiskRev(ticker, a,b,c,d)
            else:
                print("idk")
                sys.exit(1)
    else:
        print("No Internet Connection, apparently.")


if __name__ == "__main__":
    main()
