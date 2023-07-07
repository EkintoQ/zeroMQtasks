import zmq

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

for request in range(10):
    print(f"Sending request {request} …")
    socket.send(b"Hello from 1")

    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")

socket.close()
context.term()