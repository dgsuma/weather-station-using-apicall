import network, urequests
#from urllib.parse import urlencode
from parse import urlencode # uncomment the above line and comment out this one if the code above worked in the REPL
from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import utime

counter = 100

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

parameters = {
    "q":"Kadugannawa",
    "appid":"5e24cd8c46bd93234ca67c9a8c21c42a",
    "units":"metric"
}

def connect_to_wifi(wlan, ssid, password):
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

def get(url, params=None, **kw):
    if params:
        url = url.rstrip('?') + '?' + urlencode(params, doseq=True)
        print("url with parameters: " + url)
    return urequests.get(url, **kw)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

while True:
    if (counter == 100):  # Get new data every 10 minutes
        counter = 0
        lcd.backlight_on()
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Getting Data...")
        utime.sleep(4)
        connect_to_wifi(wlan, "SLT-Fiber-B00B", "Supra_Mundane@appcitizen#")
        response = get('https://api.openweathermap.org/data/2.5/weather', parameters)
        print(response.text)
        weather_data = response.json() # create a dictionary of the response content
        resTemp = str(weather_data["main"]["temp"]) # convert dictionay object to string
        resHemid = str(weather_data["main"]["humidity"]) # convert dictionay object to string
        resPressure = str(weather_data["main"]["pressure"]) # convert dictionay object to string
        resLoc = weather_data["name"]
        lcd.move_to(0, 0)
        lcd.putstr("Loc: " + resLoc)
        lcd.move_to(0, 1)
        lcd.putstr("Tem: " + resTemp + "\xDF""C")
        utime.sleep(2)
        #utime.sleep_ms(2000)
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Loc: " + resLoc)
        lcd.move_to(0, 1)
        lcd.putstr("Hum: " + resHemid + " %")
        utime.sleep(2)
        #utime.sleep_ms(2000)
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Loc: " + resLoc)
        lcd.move_to(0, 1)
        lcd.putstr("Pre: " + resPressure + " hPa")
        utime.sleep(2)
        #utime.sleep_ms(2000)
        lcd.clear()
    else:
        counter = counter + 1
        resLoc = weather_data["name"]
        lcd.move_to(0, 0)
        lcd.putstr("Loc: " + resLoc)
        lcd.move_to(0, 1)
        lcd.putstr("Tem: " + resTemp + "\xDF""C")
        utime.sleep(2)
        #utime.sleep_ms(2000)
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Loc: " + resLoc)
        lcd.move_to(0, 1)
        lcd.putstr("Hum: " + resHemid + " %")
        utime.sleep(2)
        #utime.sleep_ms(2000)
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Loc: " + resLoc)
        lcd.move_to(0, 1)
        lcd.putstr("Pre: " + resPressure + " hPa")
        utime.sleep(2)
        #utime.sleep_ms(2000)
        lcd.clear()
        
    