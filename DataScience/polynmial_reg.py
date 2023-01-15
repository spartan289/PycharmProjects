#
# import numpy as np
#
#
# class QuadraticRegression:
#     def __init__(self):
#         self.theta = np.random.randn(3, 1)
#
#     def fit(self, X, y, learning_rate=0.01, num_iterations=100):
#         for i in range(num_iterations):
#             y_pred = self.predict(X)
#             error = y_pred - y
#             theta0_grad = 2 / len(y) * np.sum(error)
#             theta1_grad = 2 / len(y) * np.sum(error * X)
#             theta2_grad = 2 / len(y) * np.sum(error * np.power(X, 2))
#             self.theta[0] -= learning_rate * theta0_grad
#             self.theta[1] -= learning_rate * theta1_grad
#             self.theta[2] -= learning_rate * theta2_grad
#
#     def predict(self, X):
#         return self.theta[0] + self.theta[1] * X + self.theta[2] * np.power(X, 2)
#
#     def mean_squared_error(self, X, y):
#         y_pred = self.predict(X)
#         return np.mean(np.power((y_pred - y), 2))
#
# quad = QuadraticRegression()
# x = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22])
# y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100])
# quad.fit(x, y)
# Y = quad.predict(x)
# print(Y)
#
# import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.plot(x, Y, color='red')
# plt.show()

# import numpy as np
#
#
#
#
# quad = QuadraticRegression()
# x = np.array([1, 2, 3, 5, 6, 7])
# y = np.array([100, 90, 80, 60, 60, 55])
# print(x.shape)
# quad.fit(x, y)
# Y = quad.predict(x)
# print(Y)
#
# import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.plot(x, Y, color='red')
# plt.show()
#
#
# X = np.array([1, 2, 3, 4, 5])
# y = np.array([3, 5, 7, 9, 11])
#
# quad_reg = QuadraticRegression()
# quad_reg.fit(X, y, learning_rate=0.01, num_iterations=1000)
#
# y_pred = quad_reg.predict(X)
#
# print("Predicted values:", y_pred)

import numpy as np

import numpy as np

# import numpy as np
#
#
# class PolynomialRegression:
#     def __init__(self, degree):
#         self.degree = degree
#
#     def fit(self, X, y, learning_rate=0.01, num_iterations=100):
#         X = self._add_polynomial_columns(X)
#         self.theta = np.random.randn(self.degree, 1)
#
#         for i in range(num_iterations):
#             gradient = self._gradient(X, y)
#             self.theta -= learning_rate * gradient
#
#     def predict(self, X):
#         X = self._add_polynomial_columns(X)
#         return X @ self.theta
#
#     def _add_polynomial_columns(self, X):
#         X_poly = np.ones((X.shape[0], self.degree))
#         for i in range(1, self.degree):
#             X_poly[:, i] = np.power(X, i).flatten()
#         print(X_poly.shape)
#         return X_poly
#
#     def _gradient(self, X, y):
#         y_pred = self.predict(X)
#         return X.T @ (y_pred - y) / len(y)
#
#
# X = np.array([1, 2, 3, 4, 5])
# X = X.reshape(-1,1)
# print(X.shape)
# y = np.array([3, 5, 7, 9, 11]).reshape(-1, 1)
# poly_reg = PolynomialRegression(degree=2)
# poly_reg.fit(X, y, learning_rate=0.01, num_iterations=1000)
#
# y_pred = poly_reg.predict(X)
#
# print("Predicted values:", y_pred)


import numpy as np

import math

import matplotlib.pyplot as plt

# Univariate Polynomial Regression

class PolynomailRegression() :

    def __init__( self, degree, learning_rate, iterations ) :

        self.degree = degree

        self.learning_rate = learning_rate

        self.iterations = iterations

    # function to transform X

    def transform( self, X ) :

        # initialize X_transform

        X_transform = np.ones( ( self.m, 1 ) )

        j = 0

        for j in range( self.degree + 1 ) :

            if j != 0 :

                x_pow = np.power( X, j )

                # append x_pow to X_transform

                X_transform = np.append( X_transform, x_pow.reshape( -1, 1 ), axis = 1 )

        return X_transform

    # function to normalize X_transform

    def normalize( self, X ) :

        X[:, 1:] = ( X[:, 1:] - np.mean( X[:, 1:], axis = 0 ) ) / np.std( X[:, 1:], axis = 0 )

        return X

    # model training

    def fit( self, X, Y ) :

        self.X = X

        self.Y = Y

        self.m, self.n = self.X.shape

        # weight initialization

        self.W = np.zeros( self.degree + 1 )

        # transform X for polynomial  h( x ) = w0 * x^0 + w1 * x^1 + w2 * x^2 + ........+ wn * x^n

        X_transform = self.transform( self.X )

        # normalize X_transform

        X_normalize = self.normalize( X_transform )

        # gradient descent learning

        for i in range( self.iterations ) :

            h = self.predict( self.X )

            error = h - self.Y

            # update weights

            self.W = self.W - self.learning_rate * ( 1 / self.m ) * np.dot( X_normalize.T, error )

        return self

    # predict

    def predict( self, X ) :

        # transform X for polynomial  h( x ) = w0 * x^0 + w1 * x^1 + w2 * x^2 + ........+ wn * x^n

        X_transform = self.transform( X )

        X_normalize = self.normalize( X_transform )

        return np.dot( X_transform, self.W )


# Driver code

def main() :

    # Create dataset
    # x = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22])
    # y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100])

    X = np.array( [ [1],[2],[3],[5],[6],[7],[8],[9],[10],[12],[13],[14],[15],[16],[18],[19],[21],[22] ] )

    Y = np.array( [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100  ] )

    # model training

    model = PolynomailRegression( degree = 10, learning_rate = 0.001, iterations = 10000 )

    model.fit( X, Y )

    # Prediction on training set

    Y_pred = model.predict( X )

    # Visualization

    plt.scatter( X, Y, color = 'blue' )

    plt.plot( X, Y_pred, color = 'orange' )

    plt.title( 'X vs Y' )

    plt.xlabel( 'X' )

    plt.ylabel( 'Y' )

    plt.show()


if __name__ == "__main__" :

    main()