import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Wysyłanie żądań do proxy
for i in range(5):
    request = "Żądanie " + str(i)
    socket.send(request.encode())

    # Odbieranie odpowiedzi od serwerów
    while True:
        response = socket.recv()
        if not socket.getsockopt(zmq.RCVMORE):
            break
        print("Odpowiedź od serwera:", response.decode())

    # Sprawdzenie ostatniej odpowiedzi
    if response:
        print("Ostatnia odpowiedź od serwera:", response.decode())
