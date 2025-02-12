from webcam import WebcamServicer
from concurrent import futures
from pb2 import webcam_service_pb2_grpc
import grpc


def serve():
    #create the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    webcam_service_pb2_grpc.add_WebcamServiceServicer_to_server(WebcamServicer(),server)
    server.add_insecure_port('[::]:50051')
    #start the server
    server.start()
    #wait for the server to stop
    server.wait_for_termination()


serve()