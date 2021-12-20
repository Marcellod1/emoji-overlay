from deepface import DeepFace
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2

class WebcamPredictor:
    def __init__(self):
        # Hand model init
        self.hand_model_path = "resources/models/hand_model"
        self.hand_model_classes = []

        # parse labels from model into a list
        f = open(self.hand_model_path + "/labels.txt", "r")
        while(line := f.readline().rstrip()):
            line_class = line.split(" ")[1]
            self.hand_model_classes.append(line_class.lower()) 
        f.close() 

        # Webcam init
        self.webcam_image_path = "resources/img/webcam.jpg"
        self.camera = cv2.VideoCapture(0)
        self.updatewebcam()


    def updatewebcam(self):
        return_value, image = self.camera.read()
        if return_value:
            cv2.imwrite(self.webcam_image_path, image)


    def predictexpression(self):
        obj = DeepFace.analyze(img_path = self.webcam_image_path, actions = ['emotion'])
        return obj['dominant_emotion']


    def predicthand(self):
        # Load the model
        model = load_model(self.hand_model_path + "/keras_model.h5")
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(self.webcam_image_path)

        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)[0]
        max_index = np.argmax(prediction)
        return self.hand_model_classes[max_index]