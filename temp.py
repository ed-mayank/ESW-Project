import urllib.request as urllib2
import json
import time


READ_API_KEY='5IPVGMC3PSIVKXX8'
CHANNEL_ID= '1840267'

D = []

while True:
    TS = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))

    response = TS.read()
    data=json.loads(response)
    l = []

    l.append(data['field5'])
    l.append(data['field6'])
    l.append(data['field1'])
    l.append(data['field2'])
    l.append(data['field3'])
    l.append(data['field4'])
    l.append(data['created_at'])
    
    D.append(l)
    print(D)

    TS.close()