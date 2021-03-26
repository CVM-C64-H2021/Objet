import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("yoy")
    else:
        print("pas yay", rc)



broker = "broker.mqttdashboard.com"
port = 1883

client = mqtt.Client("python1")
client.on_connect = on_connect

client.loop_start()

client.connect(broker, port=port)
client.publish("testlashit", "woot")

client.loop_stop()
client.disconnect()