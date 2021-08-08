for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    Bit = []
    for bit in range(31):
        count = 0
        i=0
        while i<n:
            if a[i]%2!=0:
                count+=1
            a[i]=a[i]//2
            i+=1
        Bit.append(count)

    ans=0
    for bit in range(31):
        if Bit[bit]%k==0:
            ans+=Bit[bit]//k
        else:
            ans+=Bit[bit]//k+1
    print(ans)
