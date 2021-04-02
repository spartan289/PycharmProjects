for _ in range(int(input())):
    x,y,s=input().split()
    x=int(x)
    y=int(y)
    s=s.replace('?','')
    c=0
    for i in range(len(s)-1):
        if s[i:i+2]=='CJ':
            c+=x
        elif s[i:i+2]=='JC':
            c+=y

    print("Case #{}: {}".format(_+1,c))