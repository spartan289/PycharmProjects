import numpy as np
from keras.datasets import mnist



class Network():
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.weights = [np.random.randn(y, x) for y, x in zip(sizes[1:], sizes[:-1])]
        self.bias = [np.random.randn(y, 1) for y in sizes]

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def deriv(self, y):
        return self.sigmoid(y) * (1 - self.sigmoid(y))


# network = Network([28 * 28, 10, 15, 10])
(xtrain, ytrain), (xtest, ytest) = mnist.load_data()

print(xtrain[0])