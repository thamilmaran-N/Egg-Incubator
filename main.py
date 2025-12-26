from machine import Pin, I2C
from i2c_lcd import I2cLcd
import utime
import dht
import network
import urequests

# Wi-Fi credentials
WIFI_SSID = "get password from thamilmaran"
WIFI_PASSWORD = "easypassword"

# ThingSpeak API details
THINGSPEAK_API_KEY = "BD51KPMCJ2746B79"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Pin setup
dht_sensor = dht.DHT22(Pin(16))
relay_bulb = Pin(17, Pin.OUT)
buzzer = Pin(15, Pin.OUT)

# I2C LCD setup
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Threshold values
TEMP_MIN = 37.5
TEMP_MAX = 38.0
HUMIDITY_MIN = 50
HUMIDITY_MAX = 60

# Initial settings
relay_bulb.off()
days = 0
display_alert = True

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    lcd.clear()
    lcd.putstr("Connecting to WiFi")
    while not wlan.isconnected():
        utime.sleep(1)
        lcd.putstr(".")
    lcd.clear()
    lcd.putstr("WiFi Connected")
    print("Connected to WiFi:", wlan.ifconfig())

def send_to_thingspeak(temp, humidity):
    try:
        data = {
            "api_key": THINGSPEAK_API_KEY,
            "field1": temp,
            "field2": humidity
        }
        response = urequests.post(THINGSPEAK_URL, json=data)
        print("ThingSpeak Response:", response.text)
        response.close()
    except Exception as e:
        print("Error sending to ThingSpeak:", e)

def buzzer_alert(alert_type):
    if alert_type == "low_temp":
        for _ in range(2):
            buzzer.on()
            utime.sleep(0.2)
            buzzer.off()
            utime.sleep(0.2)
    elif alert_type == "high_temp":
        for _ in range(3):
            buzzer.on()
            utime.sleep(0.1)
            buzzer.off()
            utime.sleep(0.1)
    elif alert_type == "low_humidity":
        for _ in range(2):
            buzzer.on()
            utime.sleep(0.4)
            buzzer.off()
            utime.sleep(0.4)
    elif alert_type == "high_humidity":
        for _ in range(4):
            buzzer.on()
            utime.sleep(0.1)
            buzzer.off()
            utime.sleep(0.1)

def control_system(temp, humidity):
    if temp < TEMP_MIN:
        relay_bulb.on()
    elif temp > TEMP_MAX:
        relay_bulb.off()
    else:
        relay_bulb.off()

    if humidity < HUMIDITY_MIN:
        buzzer_alert("low_humidity")
    elif humidity > HUMIDITY_MAX:
        buzzer_alert("high_humidity")

def update_lcd(temp, humidity, days, display_alert):
    lcd.clear()
    if display_alert:
        if temp < TEMP_MIN:
            lcd.putstr("Alert: LOW TEMP")
        elif temp > TEMP_MAX:
            lcd.putstr("Alert: HIGH TEMP")
        elif humidity < HUMIDITY_MIN:
            lcd.putstr("Alert: LOW HUM")
        elif humidity > HUMIDITY_MAX:
            lcd.putstr("Alert: HIGH HUM")
        else:
            lcd.putstr("System Stable")
    else:
        lcd.move_to(0, 0)
        lcd.putstr("Temp: {:.1f}C".format(temp))
        lcd.move_to(0, 1)
        lcd.putstr("Humidity: {:.1f}%".format(humidity))

connect_to_wifi()

while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        control_system(temp, humidity)
        send_to_thingspeak(temp, humidity)

        update_lcd(temp, humidity, days, display_alert)
        display_alert = not display_alert

        utime.sleep(5)

    except Exception as e:
        lcd.clear()
        lcd.putstr("Sensor Error")
        print(e)
        utime.sleep(2)
