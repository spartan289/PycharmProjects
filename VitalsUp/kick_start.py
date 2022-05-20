for _ in range(int(input())):
    n,m = map(int,input().split())
    li = list(map(int,input().split()))
    if m>sum(li):
        print("Case #{}: {}".format(_+1,m))
    else:
        print("Case #{}: {}".format(_+1,sum(li)%m))