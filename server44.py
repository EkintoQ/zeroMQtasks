import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5556")

while True:
    # Odbieranie żądania od proxy
    request = socket.recv()

    # Symulacja przetwarzania
    time.sleep(1)

    # Przygotowanie odpowiedzi
    num_responses = 3  # Liczba odpowiedzi serwera
    for i in range(num_responses-1):
        response = "Odpowiedź " + str(i+1) + " na żądanie: " + request.decode()
        socket.send(response.encode(), zmq.SNDMORE)

    # Ostatnia odpowiedź
    last_response = "Ostatnia odpowiedź na żądanie: " + request.decode()
    socket.send(last_response.encode())

