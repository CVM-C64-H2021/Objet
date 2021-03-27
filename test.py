from CameraDAO import *
from ConnectionMqtt import *

camera = CameraDAO()
camera.prendrePhoto()
# print(conversionImage("NewPicture.jpg"))
controleur = ConnectionMqtt("henry", "broker.mqttdashboard.com", 1883)
# print(controleur)
#controleur.publish("test/mqtt", conversionImage("NewPicture.jpg"))
controleur.envoyerImage("test/mqtt", "NewPicture.jpg")
