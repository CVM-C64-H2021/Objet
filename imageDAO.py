import pymongo
import base64

class imageDAO():
    def __init__(self):
        self.connection()
        self.get_next_id()
    
    def connection(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["IOT"]
        self.collection = self.db["SecurityCamera"]

    def get_next_id(self):
        self.next_id = self.collection.count() + 1
        return self.next_id

    def saveImage(self, imageName, image):
        infoImage = {}
        infoImage[imageName] = base64.b64encode(image).decode("utf-8")
        self.collection.insert_one(infoImage)

    def getAllImages(self):
        allImages = []
        for image in self.collection.find():
            allImages.append(image)
        return allImages