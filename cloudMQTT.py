import paho.mqtt.client as mqtt
import os, urllib.parse, os.path
import json
import base64

class connectionMQTT():

    def __init__(self, url, topic):
        self.mqttc = mqtt.Client()
        
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

    def publish(self,image, date):
        # Publish a message

        faceDict = {}
        faceDict["id"] = 123
        faceDict["date"] = date
        faceDict["type"] = "Detection du visage"
        faceDict["valeur"] = base64.b64encode(image).decode("utf-8")
        faceDict["alerte"] = 1
        faceDict["messageAlerte"] = "Cette personne a voulu manger vos biscuits!!!"

        #test
        f = open("test.txt", "w")
        f.write(str(base64.b64encode(image).decode("utf-8")))
        f.close()

        message = json.dumps(faceDict)

        self.mqttc.publish(self.topic, message)

    # Continue the network loop, exit when an error occurs
    #rc = 0
    #while rc == 0:
    #    rc = mqttc.loop()
    #print("rc: " + str(rc))