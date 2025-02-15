# webcam_rpc
service and client for publishing and subscribing to a video feed from a webcam

## Installing the requirements

```
pip install -r requirements.txt

```


## Compiling the Proto file
<p>If you need to recompile the .proto file you can do so by running the following:</p>

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. webcam_service.proto

```

## Starting the service

```
python service.py
```

## Starting the client

```
python client.py 
```


