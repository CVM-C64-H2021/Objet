import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time


class ConnectionMqtt():
    def __init__(self, nomUtilisateur, broker, port):
        self.broker = broker
        self.port = port
        self.nom = nomUtilisateur

    def publish(self, topic, message):
        publish.single(topic, message, hostname=self.broker)

    def connect_mqtt(self) -> mqtt:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.client = mqtt.Client(self.nom)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)

    def subscribe(self, topic):
        def on_message(client, userdata, msg):
            print(
                f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        self.client.subscribe(topic)
        self.client.on_message = on_message
        self.client.loop_forever()

    def closeConnect(self):
        self.client.disconnect()
        self.client.loop_stop()


test = ConnectionMqtt("henry", "broker.mqttdashboard.com", 1883)
test.publish("test/mqtt", "yo")
test.connect_mqtt()
test.subscribe("test/mqtt")
