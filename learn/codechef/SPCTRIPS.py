for _ in range(int(input())):
    n = int(input())
    c=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i%j==0:
                continue
            if j%(i%j)==0:
                c+=1
                print(j,i,j)
    print(c)
