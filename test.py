import cv2
from ConnectionMqtt import *


def prendrePhoto():
    # Prise d'une image a partir de la webcam
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        # Creation de l'image en jpg dans le dossier present
        cv2.imwrite("NewPicture.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()


prendrePhoto()
# print(conversionImage("NewPicture.jpg"))
controleur = ConnectionMqtt("henry", "broker.mqttdashboard.com", 1883)
# print(controleur)
#controleur.publish("test/mqtt", conversionImage("NewPicture.jpg"))
controleur.envoyerImage("test/mqtt", "NewPicture.jpg")
