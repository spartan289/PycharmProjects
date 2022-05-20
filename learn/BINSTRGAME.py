def binarygame(s: list[int],n: int):
    prevchange = False
    ans=0
    for i in range(1,n):
        if s[i]==s[i-1]:
            if s[i]==1:
                s[i]=0
                prevchange=True
            if s[i]==0:
                s[i]=1
                prevchange=True
        else:

            pass