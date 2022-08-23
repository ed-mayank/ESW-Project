from oneM2M_functions import *
import matplotlib.pyplot as plt
headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type' : 'application/json' 
}

uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
ae = "Indoor-Air-Pollution"
cnt = "Temperature"
uri_ae = uri_cse+"/"+ae
uri_cnt = uri_ae + "/" + cnt
uri = uri_cnt + "/?rcn=4" 
response = requests.get(uri, headers=headers)
inst ={}
ct_list=[]
con_list=[]
inst = json.loads(response.text)
cnt_dict=inst["m2m:cnt"]

for x in cnt_dict["m2m:cin"]:
    con_list.append(x["con"])
print(con_list)
