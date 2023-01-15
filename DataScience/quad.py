import numpy as np
x = np.array([1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22])
y = np.array([100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100])
a = -np.random.randn()
b = np.random.randn()
c = np.random.randn()

z = np.random.randn()
n=len(x)
error = np.sum([(y[i] - (a*(x[i]**2)+b*x[i]+c))**2 for i in range(len(x))])
i = 0


def eval_2nd_degree(coeffs, x):
    """
    Function to return the output of evaluating a second degree polynomial,
    given a specific x value.

    Args:
        coeffs: List containing the coefficients a,b, and c for the polynomial.
        x: The input x value to the polynomial.

    Returns:
        y: The corresponding output y value for the second degree polynomial.

    """
    a = (coeffs[0] * (x * x))
    b = coeffs[1] * x
    c = coeffs[2]
    y = a + b + c
    return y


def loss_mse(ys, y_bar):
    """
    Calculates MSE loss.

    Args:
        ys: training data labels
        y_bar: prediction labels

    Returns: Calculated MSE loss.
    """
    return sum((ys - y_bar) * (ys - y_bar)) / len(ys)


while i<1000:

    deriv_a = -(2)*np.sum((y - (a*np.power(x,2)+b*x+c))*np.power(x,2))
    deriv_b = -(2)*np.sum((y - (a*np.power(x,2)+b*x+c))*x)
    deriv_c = -(2)*np.sum((y - (a*np.power(x,2)+b*x+c)))

    step_size_a = -0.01 * deriv_a
    step_size_b = -0.01 * deriv_b
    step_size_c = -0.01 * deriv_c

    a += step_size_a
    b += step_size_b
    c += step_size_c

    i += 1
print(a,b,c,z)


import matplotlib.pyplot as plt
print(x.shape)
print(y.shape)
p = np.linspace(0,30,30)
q = a*p*p+b*p+c
plt.plot(p,q)
plt.scatter(x,y)
plt.show()
