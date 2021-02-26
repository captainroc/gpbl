#include "DHT.h"                  //匯入程式庫 DHT sensor library

#define DHTPIN 2                 // DHT pin 2 連接 Arduino pin 2
#define DHTTYPE DHT11            // 適用 DHT 11
//#define DHTTYPE DHT22          // 適用 DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21          // 適用 DHT 21 (AM2301)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  //Serial.println(F("DHT11 test!"));
  dht.begin();
}

void loop() {
  delay(2000);                             //等2秒鐘
  float h = dht.readHumidity();            //讀取濕度值 h
  float t = dht.readTemperature();         //讀取攝氏溫度值 t
  
  if (isnan(h) || isnan(t)) {                    //如果讀不到數值，印出讀取失敗訊息
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  if (h>60){
  Serial.print("alert ");
  Serial.print(h);
  Serial.println(" %\t ");
  }
  else{                                      //在序列埠螢幕中印出濕度、攝氏溫度、和華氏溫度
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" % ");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" *C ");
}
}
