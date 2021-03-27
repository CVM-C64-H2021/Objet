from CameraDAO import *
from ConnectionMqtt import *

camera = CameraDAO()
camera.prendrePhoto()
mqtt = ConnectionMqtt("henry", "broker.mqttdashboard.com", 1883)
mqtt.envoyerImage("test/mqtt", "NewPicture.jpg")
