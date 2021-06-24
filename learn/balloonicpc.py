for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    li = [i for i in range(1,8)]
    c=0
    f=0
    for i in a:
        if c==7:
            break
        f+=1
        if i in li:
            c+=1
    print(f)
