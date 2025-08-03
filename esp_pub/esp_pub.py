import network
import time
from umqtt.simple import MQTTClient

SSID = "Wokwi-GUEST"
PASSWORD = ""

BROKER = "broker.hivemq.com"
TOPIC = b"esp32/helloworld"

def wifi_conneceted():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID,PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.1)
    print("WIFI Connected")

   

def main():
    wifi_conneceted()
    client = MQTTClient("Client-ID",BROKER)
    client.connect()
    print("MQTT Connected")

    last_msg = time.ticks_ms()

    while True:
        if time.ticks_diff(time.ticks_ms(),last_msg) > 5000:
            client.publish(TOPIC,"first message!!!!!!!!",qos = 1)
            print("MSG sent successfully")
            last_msg = time.ticks_ms()
        time.sleep(0.1)

main()
    
