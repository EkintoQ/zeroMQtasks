import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} …")
    socket.send(b"Hello from 2")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")

socket.close()
context.term()