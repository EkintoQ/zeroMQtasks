import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5556")

while True:
    request = socket.recv()

    time.sleep(1)

    response = "Odpowiedź na żądanie: " + request.decode()

    socket.send(response.encode())
