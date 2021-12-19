from deepface import DeepFace
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2


class WebcamPredictor:


    def __init__(self):
        # model and image paths
        self.hand_model_path = "resources/models/keras_model.h5"
        self.webcam_image_path = "resources/img/image.jpg"
        self.camera = cv2.VideoCapture(0)
        self.updatewebcam()


    def updatewebcam(self):
        return_value, image = self.camera.read()
        if return_value:
            cv2.imwrite(self.webcam_image_path, image)


    def predictexpression(self):
        obj = DeepFace.analyze(img_path = self.webcam_image_path, actions = ['emotion'])
        print("EMOTION: {}\n".format(obj['dominant_emotion']))


    def predicthand(self):
        # Load the model
        model = load_model(self.hand_model_path)
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Replace this with the path to your image
        image = Image.open(self.webcam_image_path)
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)
        print(prediction)