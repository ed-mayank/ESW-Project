from oneM2M_functions import *
from flask import Flask, render_template, redirect, url_for, jsonify
import urllib.request as urlli
import json

uri_cse = "http://esw-onem2m.iiit.ac.in:443/~/in-cse/in-name/Team-6"
ae = "Node-1"
cnt = "Data"

headers = {
    'X-M2M-Origin': 'Li640e:eTUBds',
    'Content-type': 'application/json;ty=4'
}

ChannelId='1840267'
ReadApi='5IPVGMC3PSIVKXX8'


def CreateContainers():
    uri_ae = uri_cse+"/"+ae
    create_ae(uri_cse, ae)
    create_cnt(uri_ae,cnt)
    create_cnt(uri_ae,"Data_Description")
    create_data_cin(uri_ae+"/Data_Description","[Temperature, Humidity, CO2, VOC-Index, PM-2.5, PM-10]")

def ParseData(timestamp):
    formatstr=''
    ind=timestamp.find('T')
    
    formatstr+=timestamp[ind-2]
    formatstr+=timestamp[ind-1]
    formatstr+='/'
    formatstr+=timestamp[ind-4]
    formatstr+=timestamp[ind-3]
    formatstr+='/'
    formatstr+=timestamp[ind-8]
    formatstr+=timestamp[ind-7]
    formatstr+=timestamp[ind-6]
    formatstr+=timestamp[ind-5]
    formatstr+=' '

    c=0
    for i in range(ind+1,len(timestamp)):
        formatstr+=timestamp[i]
        c+=1
        if c%2==0 and c<5:
            formatstr+=':'
    formatstr+=' '
    return formatstr

app =Flask(__name__)
@app.route("/")
def home():
    return render_template("dashboard.html")
@app.route("/Date")
def date():
    return render_template("date.html")
@app.route("/About")
def about():
    return render_template("about.html")
@app.route("/Contact")
def contact():
    return render_template("contact.html")

@app.route("/_stuff")
def stuff():
    url=f'https://api.thingspeak.com/channels/{ChannelId}/feeds.json?api_key={ReadApi}&results=1'
    d=urlli.urlopen(url).read()
    dat=json.loads(d)
    data=dat["feeds"]
    temp=(data[0])['field5']
    hum=(data[0])['field6']
    co2=(data[0])['field1']
    voc=(data[0])['field2']
    pm2=(data[0])['field3']
    pm10=(data[0])['field4']
    

# -------------If latest data is to be fetched by oneM2M-------------------------------    
    # resp = requests.get(
    #     f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    # result = json.loads(resp.text)
    # data = result['m2m:cin']['con']
    # begin=0
    # temp=''
    # hum=''
    # co2=''
    # voc=''
    # pm2=''
    # pm10=''
    # for dat in data:
    #     if(dat==','):
    #         break
    #     if begin==1:
    #         temp+=dat
    #     if(dat=='['):
    #         begin=1
    # begin=0
    # for dat in data:
    #     if(dat==','):
    #         begin+=1
    #     if begin==1 and dat!=',':
    #         hum+=dat
    #     if(begin>1):
    #         break
    # begin=0
    # for dat in data:
    #     if(dat==','):
    #         begin+=1
    #     if begin==2 and dat!=',':
    #         co2+=dat
    #     if(begin>2):
    #         break
    # begin=0
    # for dat in data:
    #     if(dat==','):
    #         begin+=1
    #     if begin==3 and dat!=',':
    #         voc+=dat
    #     if(begin>3):
    #         break
    # begin=0
    # for dat in data:
    #     if(dat==','):
    #         begin+=1
    #     if begin==4 and dat!=',':
    #         pm2+=dat
    #     if(begin>4):
    #         break
    # begin=0
    # for dat in data:
    #     if(dat==']'):
    #         break
    #     if(dat==','):
    #         begin+=1
    #     if begin==5 and dat!=',':
    #         pm10+=dat

    # return(temp)
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])
    return jsonify(temperature=float(temp),humidity=float(hum),co2=float(co2),voc=float(voc),pm2=float(pm2),pm10=float(pm10),timestamp=data[0]['created_at'])

@app.route("/_stuff2")
def stuff2():
    url=f'https://api.thingspeak.com/channels/{ChannelId}/feeds.json?api_key={ReadApi}'
    d=urlli.urlopen(url).read()
    dat=json.loads(d)
    data=dat["feeds"]
# -------------If latest data is to be fetched by oneM2M-------------------------------    
    # resp = requests.get(
    #     f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/?rcn=4', headers=headers)
    # result = json.loads(resp.text)
    # y=result['m2m:cnt']
    # data=[]
    # for x in y['m2m:cin']:
    #     data.append(x['con']+x['ct'])

    return jsonify(data)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

