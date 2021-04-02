for _ in range(int(input())):
    n=int(input())
    x=0
    for i in range(n,n+5):
        if i%5==0:
            x=i
            break
    if x-n<3 and x>=38:
        print(x)
    elif x-n>=3 or x<=40:
        print(n)