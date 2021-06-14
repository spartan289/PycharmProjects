for _ in range(int(input())):
    n,m = map(int,input().split())
    li = input()
    li = [int(x) for x in li]
    z = []
    c=0
    for i in range(m):
        first=0
        dict={}
        x=0
        while x<len(li):
            if li[x]==0:
                if x==0:
                    if li[1] == 1:
                        dict[0]=1
                elif x==n-1:
                    if li[n-2]==1:
                        dict[n-1]=1

                elif (li[x-1] ^ li[x+1])==1:
                    dict[x]=1
            x+=1
        for i, (k, v) in enumerate(dict.items()):
            li[k]=v
        if z==li and c>1:
            break
        z=li

    str1 = ''.join(str(e) for e in li)
    print(str1)
