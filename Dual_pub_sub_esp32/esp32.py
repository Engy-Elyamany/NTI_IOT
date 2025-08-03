import network
import time
from umqtt.simple import MQTTClient

SSID = "Wokwi-GUEST"
PASSWORD = ""

BROKER = "broker.hivemq.com"
TOPIC_PUB = b"esp32/helloworld"
TOPIC_SUB = b"esp32/print"

def wifi_conneceted():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID,PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.1)
    print("WIFI Connected")

def mqtt_callback(topic,msg):
    print("Topic : ",topic,"Message : ",msg)
    if msg == b'greetings':
        print("hello")
    elif msg == b'name':
        print("ESP32")

def main():
    wifi_conneceted()
    client = MQTTClient("Client-ID",BROKER)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(TOPIC_SUB)
    print("ESP32 Subscribed successfully")
    print("MQTT Connected")

    last_msg = time.ticks_ms()

    while True:
        client.check_msg()
        if time.ticks_diff(time.ticks_ms(),last_msg) > 5000:
            client.publish(TOPIC_PUB,"STILL ALIVE")
            print("\nMSG Published successfully")
            last_msg = time.ticks_ms()
        time.sleep(0.1)

main()
    
