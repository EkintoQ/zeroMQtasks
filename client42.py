import zmq
import numpy as np
import pickle

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

matrices = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]

data = pickle.dumps(matrices)

socket.send(data)

result = socket.recv()

multiplied_matrices = pickle.loads(result)

for matrix in multiplied_matrices:
    print(matrix)
