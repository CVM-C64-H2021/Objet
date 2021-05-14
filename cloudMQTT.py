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

    def publish(self, image, date, numberOfRecognition):
        # Publish a message

        faceDict = {}
        faceDict["id"] = 123
        faceDict["idApp"] = 456
        faceDict["date"] = date
        faceDict["type"] = "image"
        faceDict["valeur"] = str(base64.b64encode(image))
        faceDict["alerte"] = 1

        if numberOfRecognition < 2:
            faceDict["alerte"] = 0
            faceDict["messageAlerte"] = "Tout est beau, commandant"
        else:
            faceDict["alerte"] = 1
            faceDict["messageAlerte"] = "Cette personne a voulu manger vos biscuits!!! C'est la " + \
                str(numberOfRecognition + 1) + "eme fois!!! &#127850"
        print(faceDict["messageAlerte"])
        message = json.dumps(faceDict)

        self.mqttc.publish(self.topic, message)
