import grpc
import cv2
import numpy as np
from pb2 import webcam_service_pb2,webcam_service_pb2_grpc

hostname = 'localhost'
filename ='image.jpg'
def single_image():
    with grpc.insecure_channel(hostname+':50051') as channel:
        stub = webcam_service_pb2_grpc.WebcamServiceStub(channel)
        #get the image response from the capture request
        response = stub.CaptureImage(webcam_service_pb2.CaptureImage(device_id=0))
        #0 is the default opencv  device id of your default webcam if your machine has one 
        print('capturing image on device:'+0)
        img = np.frombuffer(response.image_data,np.uint8)
        img = np.reshape((480,640,3))
        cv2.imwrite(filename,img)


    
