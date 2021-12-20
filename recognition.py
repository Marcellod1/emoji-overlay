from predict import WebcamPredictor

predictor = WebcamPredictor()

while(True):
    predictor.updatewebcam()
    try:
        prediction = predictor.predicthand()

        if(prediction == "neutral"):
            prediction = predictor.predictexpression()
            
        print(prediction)

    except(Exception):
        print("Predictor Error")