import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for i in range(5):
    request = "Żądanie " + str(i)
    socket.send(request.encode())

    response = socket.recv()
    print("Odpowiedź od serwera:", response.decode())
