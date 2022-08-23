
#include <WiFi.h>
#include "time.h"
#include  <ArduinoJson.h>
#include "HTTPClient.h"


//==================PINS==================
int trig = 14;
int echo = 12;
//==================Global variables======================
const char *wifi_ssid = "D-Link_DIR-615";      // your network SSID (name)
const char *wifi_pass = "ShradhaSri";   // your network password
String Temperature;
String Humidity;
String CO2;
String VOC_Index;
String PM_2;
String PM_10;
String cse_ip = "192.168.0.101";        // YOUR IP from ipconfig/ifconfig
String cse_port = "8080";
String server = "http://" + cse_ip + ":" + cse_port + "/~/in-cse/in-name/";
String ae ="Indoor-Air-Pollution";
String cnt[]= {"Temperature", "Humidity", "CO2", "VOC-Index", "PM-2.5", "PM-10"};
// =============================================================
void GetTempHumVOCReading()
{
  Temperature="37";
  Humidity="72";
  VOC_Index="12";
}
void GetPMReading()
{
  PM_2="7";
  PM_10="7";
}
void GetCO2Reading()
{
  CO2="15";
}
void ConnectToWifi()
{
  while (WiFi.status() != WL_CONNECTED) {
    
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(wifi_ssid);
    WiFi.begin(wifi_ssid, wifi_pass);
    // wait 10 seconds for connection:
    delay(10000);
  }
  Serial.print("Connected to the network with ip:");
  Serial.println(WiFi.localIP());
}
//POST Request
void CreateContentInstance(String& cnt, String& val)
{
  HTTPClient http;
  http.begin(server + ae + "/" + cnt + "/");
  http.addHeader("X-M2M-Origin", "admin:admin");
  http.addHeader("Content-Type", "application/json;ty=4");
  int code = http.POST("{\"m2m:cin\": {\"cnf\":\"application/json\",\"con\": " + val + "}}");
  Serial.println(code);
  if (code == -1) {
    Serial.println("UNABLE TO CONNECT TO THE SERVER");
  }
  http.end();
}

void setup() {
  Serial.begin(9600);
  ConnectToWifi();
}

void loop() {
  GetTempHumVOCReading();
  GetPMReading();
  GetCO2Reading();
  for(int i=0;i<6;i++)
  {
    if(i==0)
      CreateContentInstance(cnt[i],Temperature);
    if(i==1)  
      CreateContentInstance(cnt[i],Humidity);
    if(i==2)  
      CreateContentInstance(cnt[i],CO2);
    if(i==3)  
      CreateContentInstance(cnt[i],VOC_Index);
    if(i==4)  
      CreateContentInstance(cnt[i],PM_2);
    if(i==5)  
      CreateContentInstance(cnt[i],PM_10);
  }
  
  delay(1000);

}
