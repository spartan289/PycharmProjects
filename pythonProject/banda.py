#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    c=0
    d=0
    for i in range(len(a)):
            if(a[i]>b[i]):
                c+=1
            if (a[i]<b[i]):
                d+=1

                return c and d
if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)