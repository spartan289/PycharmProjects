for _ in range(int(input())):
    n,x=map(int,input().split())
    li=list(map(int,input().split()))
    litwo=[i//x for i in li ]
    d={}
    for i,v in enumerate(litwo):
        d[i]=v
    d={k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    print("Case #{}: ".format(_+1),end="")
    for i in d.keys():
        print(i+1,end=" ")
    print()