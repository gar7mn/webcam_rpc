from pb2 import webcam_service_pb2,webcam_service_pb2_grpc
import cv2

class WebcamServicer(webcam_service_pb2_grpc.WebcamServiceServicer):
    """The servicer for the webcam service"""
    
    def __init__(self):
        super(WebcamServicer,self).__init__()

    def StartStreaming(self, request, context):
        return webcam_service_pb2.StartResponse(success=True)
    
    def StopStreaming(self, request, context):
        return webcam_service_pb2.StopResponse(success=True)
    
    def CaptureImage(self, request, context):
        #capture an image and send it to the client
        cap = cv2.VideoCapture()
        ret,frame = cap.read()
        if ret:
            return webcam_service_pb2.ImageResponse(image_data=frame.tobytes())
        else:
            return webcam_service_pb2.ImageResponse(image_data=b'')
        