#include <Wire.h> // I2C程式庫
#include <LiquidCrystal_I2C.h> // LCD_I2C模組程式庫
#include "DHT.h"

// LCD I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、2為LCD顯示器大小。
LiquidCrystal_I2C lcd(0x27, 16, 2); 

// DHT init
#define DHTPIN 9 
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {

  Serial.begin(9600);
  dht.begin();  //初始化DHT

  // 初始化LCD
  lcd.init();
  lcd.backlight();
}
void loop() {

  delay(5000);
  float h = dht.readHumidity();   //取得濕度
  float t = dht.readTemperature();  //取得溫度C
  // Serial.print("Humidity: ");
  Serial.println(t);
  // Serial.print(" %\t");
  // Serial.print("Temperature: ");
  Serial.println(h);
  // Serial.println(" *C ");
  
  // lcd.clear();
  lcd.setCursor(0, 0);  //設定游標位置 (字,行)
  lcd.print("RH  :");  //Relative Humidity 相對濕度簡寫
  lcd.setCursor(7, 0);  
  lcd.print(h);
  lcd.setCursor(14, 0);
  lcd.print("%");

  lcd.setCursor(0, 1);  //設定游標位置 (字,行)
  lcd.print("Temp:");
  lcd.setCursor(7, 1);  
  lcd.print(t);
  lcd.setCursor(13, 1);
  lcd.print((char)223); //用特殊字元顯示符號的"度"
  lcd.setCursor(14, 1);
  lcd.print("C");
  
  Serial.flush();
}
