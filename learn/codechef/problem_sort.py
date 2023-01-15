n,s = map(int,input().split())
arr=[]
for _ in range(n):
    a = list(map(int,input().split()))
    b= list(map(int,input().split()))
    c = list(zip(a,b))
    sorted_c = sorted(c)
    dif_count=0
    for i in range(s-1):
        if sorted_c[i][1]>sorted_c[i+1][1]:
            dif_count+=1
    arr.append((dif_count,_))
arr = sorted(arr)
for  i in range(n):
    print(arr[i][1]+1)