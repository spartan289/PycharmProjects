for _ in range(int(input())):
    n,a,b = map(int,input().split())
    bin = input()
    c=0
    for i in bin:
        if i=='1':
            c+=1
    total = (n-c)*a +c*b
    print(total)
