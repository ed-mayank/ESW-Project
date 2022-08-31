from oneM2M_functions import *
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

# CreateContainers()
# create_data_cin(uri_cse+"/"+ae+"/"+cnt,"[1,2,3,4,5,6]")


app =Flask(__name__)
@app.route("/")
def home():
    return "Indoor Air pollution"
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
    return(temp)
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

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
    return(temp)
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

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
    return(temp)
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

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
    return(temp)
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

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
    return(temp)
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

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
        
    return(temp)  
    # return render_template("ui.html", content=float(temp),timestamp=result['m2m:cin']['ct'])

if __name__ == "__main__":
    app.run()




