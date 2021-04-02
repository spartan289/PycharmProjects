#Q1. Missing Number
# 
# def missingnum(array):
#     n=len(array)
#     sum2=sum(array)
#     sum1=n*(n+1)//2
#     print(sum1-sum2)
# missingnum([9,6,4,2,3,5,7,0,1])

#Q2. Write a program to find all pairs of integers whose sum is eqal to a given number
# def pair(array,n):
#     for i in array:
#         for j in array:
#             if i+j==n:
#                 print(i,j)
# pair([2,6,3,9,11],9)
# #q2b. same pair but differnce
# def diff(arr,n):
#     c=0
#     for i in arr:
#         pair=n+i
#         if pair in arr:
#             c+=1
#     print(c)
# diff([1,3,5,8,6,4,2],2)
#Q3. How to find maximum product of two integer in the array:
# [1,20,30,44,5]
# def maxproduct(array):
#
#     curr=array[0]*array[1]
#     for i in range(1,len(array)-1):
#         new = array[i]*array[i+1]
#         if new>curr:
#             curr=new
#     print(curr)
# maxproduct([-2])

#Q3. is unique list yes or not
# def isunique(array):
#     empty=[]
#     for i in array:
#         if i in empty:
#             return False
#         empty.append(i)
#     return True
# print(isunique([1,2,3,3,5]))

#q6. permutation
# def permutation(list1,list2):
#     list1.sort()
#     list2.sort()
#     if list1==list2:
#         print("They are permutation of each other")
# permutation([1,2,3],[2,3,1])
#q7 rotate matrix
import numpy as np
def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
print(rotate_matrix(matrix))
