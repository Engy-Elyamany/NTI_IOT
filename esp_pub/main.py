import paho.mqtt.client as mqt
from paho import mqtt
BROKER = "broker.hivemq.com"

client2 = mqt.Client()
client2.connect(BROKER,1883,60)

client2.subscribe("esp32/helloworld",qos=1)

def on_my_message(client, userdata, msg):
    print(f"Message : {str(msg.payload)} with QoS {str(msg.qos)} from Topic {msg.topic}")

client2.on_message = on_my_message

client2.loop_forever()