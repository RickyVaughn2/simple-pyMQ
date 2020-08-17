# node.py
# Simple Python client to show node activity from ttn MQTT brooker with credentials
# Author: R2
# first install paho.mqtt.client: pip install paho-mqtt
# 
import paho.mqtt.client as mqtt

#Call back functions 

# gives connection message
def on_connect(client,userdata,rc):
    print("Connected with result code:"+str(rc))
    # subscribe for all devices of user
    client.subscribe('+/devices/+/up')

# gives message from device
def on_message(client,userdata,msg):
    print"Topic",msg.topic + "\nMessage:" + str(msg.payload)

def on_log(client,userdata,level,buf):
    print("message:" + str(buf))
    print("userdata:" + str(userdata))
    
mqttc= mqtt.Client()
mqttc.on_connect=on_connect
mqttc.on_message=on_message

mqttc.username_pw_set("App-eu registered op ttn dashboard","key registered op ttn dashboard")

# - change this to your broker
mqttc.connect("my.broker.com",1883,10)

# and listen to server
run = True
while run:
    mqttc.loop()
