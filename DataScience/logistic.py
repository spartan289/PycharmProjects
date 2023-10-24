import pandas as pd
import numpy as np

X = pd.read_csv("logistic_x.txt",sep="\s+",names=["x1","x2"],header=None)
y= pd.read_csv("logistic_y.txt",sep="\s+", names=["y"], header=None, engine='python')
y=y.astype(int)
# y = np.array(y)
# X = np.array(X)
# X = np.c_[np.ones(99),X]
# X = X.reshape((99,3,1))
X = np.hstack([np.ones((X.shape[0], 1)), X[["x1","x2"]].values])
y= y["y"].values
m=99
theta = np.zeros(3)
def sigmoid(z):
    return 1/(1+np.exp(-z))
def deriv_sigmoid(z):
    return sigmoid(z)*(1-sigmoid(z))
def gradient(theta,X,y):
    z = y*X.dot(theta)
    g = -np.mean((1-sigmoid(z))*y*X.T, axis=1)
    return g
def hess(theta,X,y):
    z = y*X.dot(theta)
    hess = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            hess[i][j] = np.mean(deriv_sigmoid(z)*X[:,i]*X[:,j])
    return hess
def newton(theta,X,y):
    eps =1e-6

    delta=1
    while delta>eps:
        theta_prev = theta
        theta = theta - np.linalg.inv(hess(theta,X,y)).dot(gradient(theta,X,y))
        delta = np.linalg.norm(theta-theta_prev,ord=1)
    return theta
print(newton(theta,X,y))
import matplotlib.pyplot as plt

