# import numpy as np
# m = 1
# c = 0
# x = np.array([1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22])
# y = np.array([100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100])
#
# error = np.sum([(y[i] - (m * x[i] + c)) ** 2 for i in range(5)])
# i = 0
#
# while i<100000:
#     deriv_c = -2*np.sum((y - (m * x + c)))
#     deriv_m = -2*np.sum(x * (y - (m * x + c)))
#     step_size = -0.00001 * deriv_c
#     step_size_m = -0.0001 * deriv_m
#     c = c + step_size
#     m = m + step_size_m
#     error = np.sum([(y[i] - (m * x[i] + c)) ** 2 for i in range(5)])
#     print("Iteration " + str(i) + ": " + str(error))
#     i += 1
# print(m,c)
# import matplotlib.pyplot as plt
# print(x.shape)
# print(y.shape)
# a = np.linspace(0,30,30)
# b = m*a+c
# plt.plot(a,b)
# plt.scatter(x,y)
# plt.show()
