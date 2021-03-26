import paho.mqtt.client as mqtt
import time


class ConnectionMqtt():
    def __init__(self, nomUtilisateur):
        broker = "broker.mqttdashboard.com"
        port = 1883

        self.client = mqtt.Client(nomUtilisateur)
        self.client.on_connect = self.on_connect
        self.client.connect(broker, port=port)

    def publish(self, message):
        self.client.publish("test/mqtt", message, qos=0, retain=False)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")


test2 = ConnectionMqtt("henry")
test2.publish("test3")
