from deepface import DeepFace
import os

IMAGES_PATH = "resources\img\input"

img_files = os.listdir(IMAGES_PATH)

for file in img_files:
    # get the full path for the image file and run emotion detection on it
    full_path = (IMAGES_PATH + "\\" + file)
    obj = DeepFace.analyze(img_path = full_path, actions = ['emotion'])
    print("FILE: {}\nEMOTION: {}\n".format(file, obj['dominant_emotion']))