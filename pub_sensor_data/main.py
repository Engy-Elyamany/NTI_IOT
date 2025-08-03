import paho.mqtt.client as mqt
from paho import mqtt
BROKER = "broker.hivemq.com"
TOPIC_SUB = "esp32/temp"
TOPIC_PUB = "esp32/relay"

def on_my_connect(client,userdata,flags,rc):
    client.subscribe(TOPIC_SUB)
    print(f"\nSubscribed to {TOPIC_SUB}")

def on_my_message(client, userdata, msg):
    print(f"\nMessage : {msg.payload} from Topic {msg.topic} \n")


client2 = mqt.Client()
client2.on_connect = on_my_connect
client2.on_message = on_my_message


client2.connect(BROKER,1883,60)
client2.loop_start()

try:
    while True:
        msg = input("Type your message or press 'q' to quit ")
        if msg.lower() == 'q':
            break
        client2.publish(TOPIC_PUB,msg)
        print(f"Published to {TOPIC_PUB} : {msg} \n")
except KeyboardInterrupt:
    print("Interrupted by User\n")
finally:
    client2.loop_stop()
    client2.disconnect()
    print("Client disconnected")