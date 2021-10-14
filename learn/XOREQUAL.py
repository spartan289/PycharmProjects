for _ in range(int(input())):
    n,x = map(int,input().split())
    li = list(map(int,input().split()))
    hash = {}
    hashxor = {}
    for i in li:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
        p = i^x
        if p in hashxor:
            hashxor[p]+=1
        else:
            hashxor[p]=1

    maxxor = 0
    count = 0
    for i in hash:
        maxxor = max(maxxor,hash[i])
    if x!=0:
        for i in hashxor:
            if i in hash:
                mtemp = hashxor[i]+hash[i]
                if mtemp==maxxor and hashxor[i]<count:
                    count = hashxor[i]
                elif mtemp>maxxor:
                    maxxor = mtemp
                    count = hashxor[i]
    print(maxxor,count)
