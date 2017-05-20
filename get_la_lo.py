# -*- coding: UTF-8 -*-
import csv
import json
import urllib2
from  pymongo import MongoClient

#链接数据库
conn=MongoClient('localhost')
db=conn.taobao_tea
db=db.taobao_tea_lv

#获取mongo中每条记录的'location'
def get_list():
    f=db.find()
    for tea in f:
        yield str(tea['location'].replace(' ','').encode("utf-8"))

#调用百度api获取经纬度，注意在地名后添加"市"，因为有些时候单纯的地名会返回空值，比如"上海"，这是百度的bug
def getLocation(name):
    url= 'http://api.map.baidu.com/geocoder?address=%s%s&output=json&key=f247cdb592eb43ebac6ccd27f796e2d2'%(name,'市')
    html = urllib2.urlopen(urllib2.Request(url))
    jsons = html.read() #转化为str类型
    hjson =json.loads(jsons) #转化为dict类型
    lng_lat=['','']
    if hjson['result']:
        lng = hjson['result']['location']['lng'] # 经度
        print type(lng)
        lat = hjson['result']['location']['lat'] # 纬度
        lng_lat= [lng, lat]
        return lng_lat
    else:return lng_lat

def main():
    i=0
    with open('/Users/apple/Desktop/tea.csv', 'w') as csvfile:
        fieldnames=['name','longitude','latitude']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()

        for place in get_list():
            a=getLocation(place)
            if a[0]:   #为了排除一些空值，因为记录中有些是"日本"，"英国"等地名，无法正常返回
                writer.writerow({'name':place,'longitude':str(a[0]),'latitude':str(a[1])})
                i+=1
                print i
            else:
                print (place)
                i+=1

if __name__=='__main__':
    main()
