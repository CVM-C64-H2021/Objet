import cv2
import logging as log
import datetime as dt
from time import sleep
import os
from cloudMQTT import *
import json

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log', level=log.INFO)

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

    faces = faceCascade.detectMultiScale(
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

            img_name = "face_{}.png".format(img_counter)
            cv2.imwrite("Faces/" + img_name, frame)
            mqtt = connectionMQTT('mqtt://ghhtzpps:MwVNHJbYYirC@driver-01.cloudmqtt.com:18760', '/C64/Projet/Equipe1/Capteur')
            mqtt.publish(frame, str(dt.datetime.now()))
            img_counter += 1
            timer = None
            log.info("img: " + img_name + " at "+str(dt.datetime.now()))
            print("picture taken")

    if len(faces) == 0:
        timer = None

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
