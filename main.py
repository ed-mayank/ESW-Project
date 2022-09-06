from oneM2M_functions import *
import random
from flask import Flask, render_template, redirect, url_for, jsonify
uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
ae = "Indoor-Air-Pollution"
cnt = "Data"

headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
}

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
@app.route("/Table")
def table():
    
    return render_template("table.html")
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
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    result = json.loads(resp.text)
    data = result['m2m:cin']['con']
    begin=0
    temp=''
    hum=''
    co2=''
    voc=''
    pm2=''
    pm10=''
    for dat in data:
        if(dat==','):
            break
        if begin==1:
            temp+=dat
        if(dat=='['):
            begin=1
    begin=0
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==1 and dat!=',':
            hum+=dat
        if(begin>1):
            break
    begin=0
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==2 and dat!=',':
            co2+=dat
        if(begin>2):
            break
    begin=0
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==3 and dat!=',':
            voc+=dat
        if(begin>3):
            break
    begin=0
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==4 and dat!=',':
            pm2+=dat
        if(begin>4):
            break
    begin=0
    for dat in data:
        if(dat==']'):
            break
        if(dat==','):
            begin+=1
        if begin==5 and dat!=',':
            pm10+=dat

    # return(temp)
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])
    return jsonify(temperature=float(temp),humidity=float(hum),co2=float(co2),voc=float(voc),pm2=float(pm2),pm10=float(pm10),timestamp=result['m2m:cin']['ct'])

@app.route("/_stuff2")
def stuff2():
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/?rcn=4', headers=headers)
    result = json.loads(resp.text)
    y=result['m2m:cnt']
    data=[]
    for x in y['m2m:cin']:
        data.append(x['con']+x['ct'])

    return jsonify(content=data)


@app.route("/Temperature")
def Temperature():
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    result = json.loads(resp.text)
    data = result['m2m:cin']['con']
    begin=0
    temp=''
    for dat in data:
        if(dat==','):
            break
        if begin==1:
            temp+=dat
        if(dat=='['):
            begin=1
    # return(temp)
    return render_template("dashboard.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

@app.route("/Humidity")
def Humidity():
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    result = json.loads(resp.text)
    data = result['m2m:cin']['con']
    begin=0
    temp=''
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==1 and dat!=',':
            temp+=dat
        if(begin>1):
            break
    # return(temp)
    print("heloo",temp)
    return render_template("humidity.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

@app.route("/CO2")
def CO2():
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    result = json.loads(resp.text)
    data = result['m2m:cin']['con']
    begin=0
    temp=''
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==2 and dat!=',':
            temp+=dat
        if(begin>2):
            break
    # return(temp)
    return render_template("CO2.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

@app.route("/VOC")
def VOC():
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    result = json.loads(resp.text)
    data = result['m2m:cin']['con']
    begin=0
    temp=''
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==3 and dat!=',':
            temp+=dat
        if(begin>3):
            break
    # return(temp)
    return render_template("VOC.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

@app.route("/PM_2")
def PM2():
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    result = json.loads(resp.text)
    data = result['m2m:cin']['con']
    begin=0
    temp=''
    for dat in data:
        if(dat==','):
            begin+=1
        if begin==4 and dat!=',':
            temp+=dat
        if(begin>4):
            break
    # return(temp)
    return render_template("pm2.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

@app.route("/PM_10")
def PM10():
    resp = requests.get(
        f'http://127.0.0.1:8080/~/in-cse/in-name/{ae}/{cnt}/la', headers=headers)
    result = json.loads(resp.text)
    data = result['m2m:cin']['con']
    begin=0
    temp=''
    for dat in data:
        if(dat==']'):
            break
        if(dat==','):
            begin+=1
        if begin==5 and dat!=',':
            temp+=dat
        
    # return(temp)  
    return render_template("pm10.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

@app.route("/random",methods=["GET"])
def random_number():
    

    z=jsonify(result=random.randint(0,20))
    return render_template("random.html",content=z)
if __name__ == "__main__":
    app.run()

