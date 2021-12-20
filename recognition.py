from predict import WebcamPredictor
import tkinter as tk
from PIL import ImageTk, Image


predictor = WebcamPredictor()
root = tk.Tk()
root.attributes('-alpha', 1.0)
root.geometry("600x600")
root.title("Emoji Overlay")

img = ImageTk.PhotoImage(Image.open(predictor.webcam_image_path))
img_label = tk.Label(root, image=img)

text = tk.StringVar()
text_label = tk.Label(root, textvariable=text, font=("Times New Roman", 25))
text.set("Marcello")

img_label.grid(row = 0, column = 0)
text_label.grid(row = 1, column = 0)

while(1):
    # update window image
    predictor.updatewebcam()

    img=ImageTk.PhotoImage(Image.open(predictor.webcam_image_path))
    img_label.configure(image=img)
    img_label.image=img
    root.update()

    try:
        prediction = predictor.predictexpression()
        print(prediction)

    except(Exception):
        print("Predictor Error")