for _ in range(int(input())):
    n,x,k=map(int,input().split())
    # noinspection PyRedeclaration
    flag='NO'
    # for i in range(n+2):
    #     if k*i==x or n+1-k*i==x:
    #         flag="YES"
    #         break
    # print(flag)
    if x>=0 and x<=n+1:
        i=((n+1)-x)/k
        if i.is_integer():
            flag='YES'
        j=x/k
        if j.is_integer():
            flag='YES'
    print(flag)