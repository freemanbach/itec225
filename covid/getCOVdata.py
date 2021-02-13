#!/bin/env python

"""
author     : freeman
date       : 20201030
desc       : Pull covid data from covidtracking.com over json api
           : it will generate a csv file after it ran.
exec       : python3 getCOVdata.py US_state || all
example    : python3 getCOVdata.py nc
example    : python3 getCOVdata.py all
"""


# global variable for state abbr codes
scode = ['ak', 'al', 'ar','az', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'ia', 'id', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'me', 'mi', 'mn', 'mo',
        'ms', 'mt', 'nc', 'nd', 'ne', 'nh', 'nj', 'nm', 'nv', 'ny', 'oh', 'ok', 'or', 'pa',  'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'va', 'vt', 'wa', 'wi',  'wv', 'wy' ]


try:
    from tqdm import trange, tqdm
except ImportError as herr:
    print("Missing tqdm lib.")


try:
    from requests.exceptions import HTTPError
    import requests
except ImportError as herr:
    print("Missing requests library")


from datetime import datetime
import json
import sys


def fixdate(d):
    # sublimate Date
    dateitem = datetime(year=int(d[0:4]), month=int(d[4:6]), day=int(d[6:8]))
    dt = str(dateitem.year)+"-"+str(dateitem.month)+"-"+str(dateitem.day)
    return dt


def chkStates(a):
    if a.strip().lower() in scode:
        return True
    else:
        return False


def all():
    for i in scode:
        a = pullJSON(i)
        x, y, z = processJSON(a)
        writeData(x,y,z, str(i))


def pullJSON(sa):
    # Having flexible US State Abbreviation to generate csv file
    if not chkStates(sa):
        print("Enter the correct 2 characters US state code!")
        sys.exit()
    state = "https://api.covidtracking.com/v1/states/" + sa + "/daily.json"
    try:
        resp = requests.get(state)
        resp.raise_for_status()
        jsondata = resp.text
    except HTTPError as herr:
        print("Http Connection Error", herr)
        sys.exit()

    return jsondata


def processJSON(jsdata):
    # more data Attributes to consider in the future, perhaps
    # date, positive, hospitalizedCumulative, death, deathConfirmed, positiveIncrease, total
    # vapos, vahospcum, vaposinc, vahospinc = [], [], [], [], [], [], []
    vadate,  vadeath, vadeathconfirm = [], [], [] 
    data = json.loads(jsdata)
    for i in data:
        if len(str(i['date'])) == 8:
            vadate.append(fixdate(str(i['date'])))
        if str(i['death']).isdigit():
            vadeath.append(int(i['death']))
        else:
            vadeath.append(0)
        if str(i['deathConfirmed']).isdigit():
            vadeathconfirm.append(int(i['deathConfirmed']))
        else:
            vadeathconfirm.append(0)
    # reverse data points
    vadeathconfirm.reverse()
    vadate.reverse()
    vadeath.reverse()

    return vadate, vadeath, vadeathconfirm
    

def writeData( a, b, c, nf ):
    # heading for csv file to prep for plotly.JS
    # Date,VADATA.Death,VADATA.DeathConfirmed
    data = []
    fn = nf.strip() + "data.csv" 
    for i in list(range(0, len(a))):
        m = str(a[i]).strip() + "," + str(b[i]).strip() + "," + str(c[i]).strip() + "\n"
        data.append(m)

    head = "Date,"+ nf.upper() + "DATA.Death," +  nf.upper() + "DATA.DeathConfirmed\n"
    
    data.insert(0, head)
    with open(fn, "w+") as f:
        for i in tqdm(data, total=len(data), desc=fn):
            f.write(i)


def main():
    network = 0
    # Forbidden Magik
    try:
        r = requests.get('https://www.google.com', timeout=4)
        network = 1
    except (requests.ConnectionError, requests.Timeout):
        network = 0

    if network == 1:
        # VOODOO Magik
        if len(sys.argv) == 2:
            xz = sys.argv
            if str(xz[1]).strip().lower() == 'all':
                all()
            else:
                a = pullJSON(str(xz[1]).strip().lower())
                x,y,z = processJSON(a)
                writeData( x, y, z, str(xz[1]))
        else:
            print("not enough parameters.")
            sys.exit()
    else:
        print("No internet Access, Apparently.")
        sys.exit()


if __name__ == "__main__":
    main()