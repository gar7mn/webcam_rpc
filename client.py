import grpc
import cv2
import numpy as np
import webcam_service_pb2_grpc
import webcam_service_pb2

hostname = 'localhost'
filename ='image.jpg'
def single_image():
    with grpc.insecure_channel(hostname+':50051') as channel:
        stub = webcam_service_pb2_grpc.WebcamServiceStub(channel)
        #get the image response from the capture request
        device='0'
        response = stub.CaptureImage(webcam_service_pb2.ImageRequest(device_id=device))
        #0 is the default opencv  device id of your default webcam if your machine has one 
        print('capturing image on device:0')
        img = np.frombuffer(response.image_data,np.uint8)
        img = np.reshape(img,(480,640,3))
        cv2.imwrite(filename,img)


    
single_image()