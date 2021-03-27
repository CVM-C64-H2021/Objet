from CameraDAO import *
from ConnectionMqtt import *

camera = CameraDAO()
camera.prendrePhoto()
controleur = ConnectionMqtt("henry", "broker.mqttdashboard.com", 1883)
controleur.envoyerImage("test/mqtt", "NewPicture.jpg")
