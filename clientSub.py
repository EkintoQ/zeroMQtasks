import zmq

context = zmq.Context()
subscriber_socket = context.socket(zmq.SUB)
subscriber_socket.connect("tcp://localhost:5555")

topic = "weather"
subscriber_socket.setsockopt_string(zmq.SUBSCRIBE, topic)

while True:
    message = subscriber_socket.recv_string()
    print(f"Received: {message}")
