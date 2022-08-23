from oneM2M_functions import *
def getContent(container):
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type' : 'application/json' 
    }
    uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
    ae = "Indoor-Air-Pollution"
    cnt = container
    uri_ae = uri_cse+"/"+ae
    uri_cnt = uri_ae + "/" + cnt
    uri = uri_cnt + "/?rcn=4" 
    response = requests.get(uri, headers=headers)
    con_list=[]
    inst = json.loads(response.text)
    cnt_dict=inst["m2m:cnt"]

    for x in cnt_dict["m2m:cin"]:
        con_list.append(x["con"])
    return con_list

def CreateContainers():
    uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
    ae = "Indoor-Air-Pollution"
    containers=["Temperature", "Humidity", "CO2", "VOC-Index", "PM-2.5", "PM-10"]
    uri_cnt=[]
    uri_ae = uri_cse+"/"+ae
    create_ae(uri_cse, ae)
    for cnt in containers:
        uri_cnt.append(uri_ae + "/" + cnt)
        create_cnt(uri_ae,cnt)

containers=["Temperature", "Humidity", "CO2", "VOC-Index", "PM-2.5", "PM-10"]

