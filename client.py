from predict import WebcamPredictor
import socket
import time

SERVER_HOST = '127.0.0.1'  # The server's hostname or IP address
SERVER_PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    predictor = WebcamPredictor()
    
    s.connect((SERVER_HOST, SERVER_PORT))
    
    while 1:
        predictor.updatewebcam()
        try:
            prediction = predictor.predictexpression()
        
            # if(prediction == "neutral"):
            #     prediction = predictor.predicthand()

        except(Exception):
            prediction = "neutral"

        #print(prediction)
        s.send((prediction + " ").encode())
        time.sleep(0.5)



