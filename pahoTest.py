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
        self.client.publish("test/mqtt", message)

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("yoy")
        else:
            print("pas yay", rc)


test2 = ConnectionMqtt("henry")
test2.publish("test3")
