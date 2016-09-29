from bottle import route, run
import json
import requests
import dateutil.parser

def getHebcal(zip):
    url = "http://www.hebcal.com/shabbat"
    #Params assume m=0 - no havdalah, b=18 - 18 mins before shabbat, a=on - ashkanaz transliterations
    #More detail: https://www.hebcal.com/home/197/shabbat-times-rest-api
    params = {'cfg':'json','m':50,'b':18,'zip':zip,'a':'on'}
    r = requests.get(url,params=params)
    return json.loads(r.text) 

def shabbat_starts(date,time):
    # I should probably clean this up
    print("Shabbat Starts: " + date + " " + time)
    
def havdalah_starts(date,time):
    # I should probably clean this up
    print("Havdalah Starts: " + date + " " + time)

def getCandleTime(obj): 
    candle = obj['items'][0]
    #Validate the api response is as expected and print candle times.
    try: 
        candle['category'] == 'candles'
    except ValueError:
        print("Expected position 0 to be candles, it's not. The API Changed.")
    else:
        shabbat_starts(formatDate(candle['date']),formatTime(candle['date']))

def getHavdalahTime(obj):
    havdalah = obj['items'][2]
    #Validate the api response is as expected and print havdalah times.
    try: 
        havdalah['category'] == 'havdalah'
    except ValueError:
        print("Expected position 2 to be havdalah, it's not. The API Changed.")
    else:
        havdalah_starts(formatDate(havdalah['date']),formatTime(havdalah['date']))
        
def formatDate(dt):
    dt_obj = dateutil.parser.parse(dt)
    date = dt_obj.strftime('%A, %B %d')
    return date

def formatTime(dt):
    dt_obj = dateutil.parser.parse(dt)
    time = dt_obj.strftime('%I:%M %p')
    return time

getCandleTime(getHebcal(11803))
getHavdalahTime(getHebcal(11803))
#TODO: Fix havdalah time
