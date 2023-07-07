import zmq

context = zmq.Context()
dealer_socket = context.socket(zmq.DEALER)
dealer_socket.identity = b"Dealer1"

dealer_socket.connect("tcp://localhost:5556")

for request_num in range(5):
    request = f"Request {request_num}".encode()
    dealer_socket.send(request)

    reply = dealer_socket.recv()
    print(f"Received reply for request {request_num}: {reply.decode()}")

dealer_socket.close()
context.term()
