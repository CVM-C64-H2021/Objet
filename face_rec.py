import face_recognition as fr
import os
import numpy as np
from time import sleep


class FaceRec:

    def get_encoded_faces(self):
        """
        looks through the faces folder and encodes all
        the faces

        :return: dict of (name, image encoded)
        """
        encoded = {}

        for dirpath, dnames, fnames in os.walk("./Faces"):
            for f in fnames:
                if f.endswith(".jpg") or f.endswith(".png"):
                    face = fr.load_image_file("Faces/" + f)
                    encoding = fr.face_encodings(face)[0]
                    encoded[f.split(".")[0]] = encoding

        return encoded

    def classify_face(self, img):
        """
        will find all of the faces in a given image and label
        them if it knows what they are

        :param im: str of file path
        :return: list of face names
        """
        faces = self.get_encoded_faces()
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())

        face_locations = fr.face_locations(img)
        unknown_face_encodings = fr.face_encodings(img, face_locations)

        face_names = []
        numberOfMatches = 0
        for face_encoding in unknown_face_encodings:
            # See if the face is a match for the known face(s)
            matches = fr.compare_faces(faces_encoded, face_encoding)

            for i in matches:
                if i == True:
                    numberOfMatches += 1

        return numberOfMatches
