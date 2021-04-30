import paho.mqtt.client as paho
import os
import urllib.parse
import os.path
import json
import base64
import cv2


class ConnectionMQTT():

    def __init__(self, url, topic):
        self.mqttc = paho.Client()

        # Parse CLOUDMQTT_URL (or fallback to localhost)
        self.url_str = os.environ.get('CLOUDMQTT_URL', url)
        self.url = urllib.parse.urlparse(self.url_str)
        self.topic = self.url.path[1:] or topic

        self.connection()

    def connection(self):
        # Connect
        self.mqttc.username_pw_set(self.url.username, self.url.password)
        self.mqttc.connect(self.url.hostname, self.url.port)

        # Start subscribe, with QoS level 0
        self.mqttc.subscribe(self.topic, 0)
        #self.mqttc.on_message = self.on_message
#
        # Continue the network loop, exit when an error occurs
        #rc = 0
        # while rc == 0:
        #    rc = self.mqttc.loop()

    def publish(self, image, date, numberOfRecognition):
        # Publish a message

        faceDict = {}
        faceDict["idApp"] = 123
        faceDict["date"] = date
        faceDict["type"] = "image"
        faceDict["valeur"] = base64.b64encode(image).decode("utf-8")
        faceDict["alerte"] = 1

        if numberOfRecognition == 0:
            faceDict["messageAlerte"] = "Cette personne a voulu manger vos biscuits!!!"
        else:
            faceDict["messageAlerte"] = "Cette personne a voulu manger vos biscuits!!! C'est la " + \
                str(numberOfRecognition + 1) + "eme fois!!!"
        print(faceDict["messageAlerte"])
        message = json.dumps(faceDict)

        self.mqttc.publish(self.topic, message)

    def on_message(self, client, obj, msg):
        message = json.dumps(msg.payload.decode("utf-8"))
        print(type(json.loads(message)))  # string?
