for _ in range(int(input())):
    n=int(input())
    s=input()
    s=list(map(int,s))
    x=0

    flag=0
    c=0
    for i in range(n):
        c+=s[i]
        x=x+1
        if (c*100)/x>=50:
            flag=1
            break

    if(flag==1):
        print("YES")
    else:
        print("NO")