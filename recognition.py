from predict import WebcamPredictor

predictor = WebcamPredictor()
predictor.updatewebcam()
prediction = predictor.predictexpression()


print(prediction)