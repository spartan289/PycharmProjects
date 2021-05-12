for _ in range(int(input())):
    n=int(input())
    s=input()
    c=1
    li=[]
    for i in range(n):
        if i!=0 and ord(s[i-1])<ord(s[i]):
            li.append(c+1)
        else:
            c=0
            li.append(c+1)
        c+=1
    print("Case #{}: ".format(_+1),end="")
    for i in li:
        print(i,end=" ")
    print()
    