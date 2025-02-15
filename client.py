# import grpc
# import cv2
# import numpy as np
# import webcam_service_pb2_grpc
# import webcam_service_pb2

# hostname = 'localhost'
# filename ='image.jpg'
# def single_image():
#     with grpc.insecure_channel(hostname+':50051') as channel:
#         stub = webcam_service_pb2_grpc.WebcamServiceStub(channel)
#         #get the image response from the capture request
#         device='0'
#         response = stub.CaptureImage(webcam_service_pb2.ImageRequest(device_id=device))
#         #0 is the default opencv  device id of your default webcam if your machine has one 
#         print('capturing image on device:0')
#         img = np.frombuffer(response.image_data,np.uint8)
#         img = np.reshape(img,(480,640,3))
#         cv2.imwrite(filename,img)

# def generate_reqs():
#     while True:
#         yield webcam_service_pb2.ImageRequest(device_id='0')
# def stream_video():
#     with grpc.insecure_channel(hostname+':50051') as channel:
#         stub = webcam_service_pb2_grpc.WebcamServiceStub(channel)
#         device = '0'
#         requests =  iter([webcam_service_pb2.ImageRequest(device_id=device)])
#         # request_iterator = iter(stub.CaptureImage(webcam_service_pb2.ImageRequest(device_id=device)))
#         response_stream = stub.ImageStream(generate_reqs())
#         for response in response_stream:
#             print(type(response))
#         # img = np.frombuffer(response.image_data,np.uint8)
#         # img = np.reshape(img,(480,640,3))
#         # cv2.imshow('stream',img)
#         #figure out how to display this stream

# stream_video()

import cv2
import grpc
import numpy as np
import webcam_service_pb2
import webcam_service_pb2_grpc

def generate_image_requests():
    while True:
        yield webcam_service_pb2.ImageRequest()

def stream_video():
    channel = grpc.insecure_channel('localhost:50051')
    stub = webcam_service_pb2_grpc.WebcamServiceStub(channel)
    response_stream = stub.ImageStream(generate_image_requests())

    for response in response_stream:
        nparr = np.frombuffer(response.image_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow('Video Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    stream_video()
