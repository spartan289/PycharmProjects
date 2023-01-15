def remone(a:list,b:list,n: int):
    sum_b=  sum(b)
    min_num=1e9
    for i in range(n):
        x=sum_b-sum(a)+a[i]
        if x%(n-1)==0 and x//(n-1)>0:
            min_num=min(min_num,x//(n-1))
    print(min_num)
for  _ in range(int(input())):
    n= int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    remone(a,b, n)
