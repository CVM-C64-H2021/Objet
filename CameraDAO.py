import cv2


class CameraDAO():

    def prendrePhoto(self):
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
