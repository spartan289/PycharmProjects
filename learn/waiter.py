#!/bin/python3

import math
import os
import random
import re
import sys


# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes


def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    li = []
    for p in range(2,n+1):
        if prime[p]:
            li.append(p)
    return li
def waiter(number, q):
    prime = SieveOfEratosthenes(10**4)
    stackA = []
    stackB = []
    index = 0
    answer = []
    for i in range(q):
        while len(number)!=0:
            x = number.pop()
            if x%prime[index]==0:
                stackB.append(x)
            else:
                stackA.append(x)
        while len(stackB)!=0:
            answer.append(stackB.pop())
        while len(stackA)!=0:
            number.append(stackA.pop(0))
        index+=1
    while len(number)!=0:
        answer.append(number.pop())
    print(answer)






if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)
