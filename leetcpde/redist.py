# # def isSubSequence(str1, str2):
# #     m = len(str1)
# #     n = len(str2)
# #     s = set()
# #     j = 0
# #     i = 0
# #     while j < m and i < n:
# #         if str1[j] == str2[i]:
# #             s.add(i)
# #             j = j + 1
# #         i = i + 1
# #     print(s)
# #
# # print(isSubSequence("ab","abcab"))
# rm = [3,1,0]
# def triplet(a,b):
#     def transpose(A):
#         B = [[0 for x in range(len(A[0]))] for y in range(len(A[0]))]
#         for i in range(len(A[0])):
#             for j in range(len(A)):
#                 B[i][j] = A[j][i]
#         return B
#     A = transpose(a)
#     x = []
#     y = []
#     z = []
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             if b[0] == A[i][j]:
#                 x.append(j)
#             if b[1] == A[i][j]:
#                 y.append(j)
#             if b[2] == A[i][j]:
#                 z.append(j)
#     print(x)
#     print(y)
#     print(z)
# 
# triplet([[2,5,3],[1,8,4],[1,7,5]],[2,7,5])

def minOperation(arr, N):

    cntMinOP = 0;

    M = len(arr[0]);

    hash = [[0 for i in range(M)] for j in range(256)]
    for i in range(N):

        for j in range(M):
            hash[ord(arr[i][j])][j] += 1;

    for i in range(M):

        Sum = 0;

        Max = 0;

        for j in range(256):
            Sum += hash[j][i];

            Max = max(Max, hash[j][i]);

        cntMinOP += (Sum - Max);
    return cntMinOP;
print(minOperation(["abc","abc","cbc"],3))
def mergetriplet(triplets,target):
    x=[]
    for triple in triplets:
        if triple[0]>target[0] or triple[1]>target[1] or triple[2]>target[2]:
            continue
        if triple[0]==target[0] and  triple[1] == target[1] and triple[2]==target[2]:
            return True
        x.append(triple)
    a=0
    b=0
    c=0
    for triple in x:
        a = max(a,triple[0])
        b = max(b,triple[1])
        c = max(c,triple[2])
    return a==target[0] and b == target[1] and c == target[2]
print(mergetriplet([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]))