for _ in range(int(input())):
    r, s = map(int, input().split()) #a is first term of r
    bs = r*s-r-1 #starting point of bs
    no=s-1
    c=0
    a=r
    n=0
    lil=[]
    lir=[]
    while (a!=1):
        if (c >= no):
            a -= 1
            c = 0
        if a==1:
            continue
        lil.append(a)
        lir.append(bs-a)
        bs-=1
        n+=1
        c+=1

    print("Case #{}: {}".format(_+1,n))
    for i in range(n):
        print(lil[i],lir[i])
