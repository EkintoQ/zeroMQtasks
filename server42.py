import zmq
import pickle

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

constant_factor = 2

while True:
    data = socket.recv()

    matrices = pickle.loads(data)

    multiplied_matrices = [constant_factor * matrix for matrix in matrices]

    result = pickle.dumps(multiplied_matrices)

    socket.send(result)
