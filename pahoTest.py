import paho.mqtt.client as mqtt

broker = "broker.mqttdashboard.com"

client = mqtt.Client("python1")
print("yooooo", client)
client.connect(broker)

