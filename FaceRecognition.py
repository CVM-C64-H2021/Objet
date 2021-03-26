import cv2
print(cv2.__file__)

class FacialRecognition:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('C:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')

        while True:
            check, frame = self.cam.read()
            faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)

            for x,y,w,h in faces:
                frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

                cv2.imshow("FaceDetection", frame)

                key = cv2.waitKey(1)

                if key == ord("q"):
                    break

        

        self.cam.release()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    main = FacialRecognition()