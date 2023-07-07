import zmq

context = zmq.Context()
router_socket = context.socket(zmq.ROUTER)
router_socket.bind("tcp://*:5556")

while True:
    identity, request = router_socket.recv_multipart()
    print(f"Received request from {identity.decode()}: {request.decode()}")

    reply = f"Reply to {request.decode()}".encode()
    router_socket.send_multipart([identity, b"", reply])
