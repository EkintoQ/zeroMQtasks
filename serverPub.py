import zmq
import time

context = zmq.Context()
publisher_socket = context.socket(zmq.PUB)
publisher_socket.bind("tcp://*:5555")

topic = "weather"
while True:
    message = f"{topic} - {time.ctime()}"
    publisher_socket.send_string(message)
    print(f"Published: {message}")
    time.sleep(1)

