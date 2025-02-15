import webcam_service_pb2
import webcam_service_pb2_grpc
import cv2
import numpy as np

class WebCamService(webcam_service_pb2_grpc.WebcamServiceServicer):
    def __init__(self):
        super(WebCamService,self).__init__()

    def CaptureImage(self, request, context):
        """Capture a single image"""
        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()
        if ret:
            #Encode the image data
            _,buffer =cv2.imencode('.jpg',frame)
            #convert the image to a bytes like object
            image_data = buffer.tobytes()
        return webcam_service_pb2.ImageResponse(image_data=image_data)
    
    def ImageStream(self, request_iterator, context):
        """Capture video"""
        cap = cv2.VideoCapture(0)
        while True:
            ret,frame = cap.read()
            if not ret:
                break
            _,buffer = cv2.imencode('.jpg',frame)
            #convert the fram to a bytes like object
            image_data = buffer.tobytes()
            yield webcam_service_pb2.ImageResponse(image_data=image_data)
        cap.release()
        