import cv2
import grpc
from concurrent import futures
import time
import webcam_service_pb2
import webcam_service_pb2_grpc
from webcam import WebCamService

def serve():
    """define the server side"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    webcam_service_pb2_grpc.add_WebcamServiceServicer_to_server(WebCamService(),server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
