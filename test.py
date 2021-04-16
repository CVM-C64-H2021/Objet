from CameraDAO import *
from cloudMQTT import *

#camera = CameraDAO()
#camera.prendrePhoto()
mqtt = connectionMQTT()
mqtt.publish("NewPicture.jpg")
