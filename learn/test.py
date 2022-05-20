import math
import matplotlib.pyplot as plt
def graph(x):
    l = len(x)
    range = max(x)-min(x)
    i = math.sqrt(l)
    b = int(range/i)
    plt.hist(x,bins = [0,10,20,30,40,50])
    plt.show()
x = [1,2,3,4,5,6,7,8,9,12,23,13,14,15,24,26,27,28]
graph(x)