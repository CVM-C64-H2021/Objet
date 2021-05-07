import cv2
import datetime as dt
from time import sleep
import os
from cloudMQTT import *
import json
from face_rec import *
import numpy as np
from imageDAO import imageDAO
import base64
from PIL import Image
from io import BytesIO
import glob


class FaceDetect:
    def __init__(self):
        self.faceRec = FaceRec()
        self.cascPath = "haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.imageDAO = imageDAO()
        self.mqtt = ConnectionMQTT(
            'mqtt://ghhtzpps:MwVNHJbYYirC@driver-01.cloudmqtt.com:18760', '/C64/Projet/Equipe1/Capteur')

    def getImagesDB(self):
        files = glob.glob("Faces/*")
        for f in files:
            os.remove(f)

        images = self.imageDAO.getAllImages()

        if len(images) > 0:
            for image in images:
                idValue = list(image.keys())
                imageValue = list(image.values())

                imageData = base64.b64decode(imageValue[1])
                bImg = BytesIO(imageData)
                img = Image.open(bImg)
                img.save("Faces/face_" + idValue[1] + ".jpg", "JPEG")

    def cameraSecurite(self):
        self.getImagesDB()

        path, dirs, files = next(os.walk(".\Faces"))
        file_count = len(files)

        video_capture = cv2.VideoCapture(0)
        img_counter = file_count
        timer = None

        while True:
            if not video_capture.isOpened():
                print('Unable to load camera.')
                sleep(5)
                pass

            # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            k = cv2.waitKey(1)

            if k % 256 == 27:
                # ESC TO QUIT
                break

            if len(faces) > 0 and timer == None:
                timer = dt.datetime.now()

            if len(faces) > 0 and timer != None:
                timerCounter = dt.datetime.now()
                diff = timerCounter - timer

                if diff.seconds >= 5.0:

                    dsize = (320, 240)
                    # resize image
                    frame = cv2.resize(frame, dsize)

                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    numberOfRecognition = self.faceRec.classify_face(frame)
                    img_name = "face_{}.jpg".format(img_counter)
                    cv2.imwrite("Faces/" + img_name, gray)

                    img = cv2.imencode('.jpg', gray)[1].tostring()

                    self.imageDAO.saveImage(img)
                    self.mqtt.publish(img, str(dt.datetime.now()),
                                      numberOfRecognition)
                    img_counter += 1
                    timer = None
                    print("picture taken")

            if len(faces) == 0:
                timer = None

            # Display the resulting frame
            cv2.imshow('Video', frame)

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
