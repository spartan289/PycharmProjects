n=int(input("enter number of rows"))
for i in range(1,n):
    for j in range(n,0,-1):
       if j>i:
           print(" ",end=" ")
       else:
           print("*",end=" ")
    print()
