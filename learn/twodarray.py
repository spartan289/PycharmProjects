import numpy as np
twoDarray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
newTwoDarray = np.insert(twoDarray, 0,[[1,2,3,4]],axis=1)
print(newTwoDarray)
# matrix = [input().split() for i in range(no_of_rows)] # if only row is given and the number of coloumn has to be decide by user
# matrix= [[input() for j in range(no_of_cols)] for i in range(no_of_rows)] # if both row and coloumn has been taken as input from user


# def accessElement(array,rowindex,colindex):
#     if rowindex >=len(array) and colindex >=len(array[0]):
#         print("Incorrect Index")
#     else:
#         print(array[rowindex][colindex])
# accessElement(twoDarray,1,2)

