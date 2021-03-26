import paho.mqtt.client as mqtt
import time

connected = False
messageOk = False


broker = "broker.mqttdashboard.com"
port = 1883

client = mqtt.Client("python1")

print("yooooo", client)

client.connect(broker, port=port)
client.loop_start()
client.publish("testlashit", "woot")
client.loop_stop()
client.disconnect()