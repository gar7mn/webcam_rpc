# webcam_rpc
service and client for publishing and subscribing to a video feed from a webcam


## Compiling the Proto file

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. webcam_service.proto

```
