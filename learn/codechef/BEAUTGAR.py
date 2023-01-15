def checkgar(s):
    n = len(s)
    if n%2!=0:
        return False
    c_r=0
    c_g=0
    for i in range(n):
        if s[i]=='R':
            c_r+=1
        else:
            c_g+=1

    if c_r!=c_g:
        return False
    else:
        c=0
        for i in range(-1,n-1):
            if s[i]==s[i-1]:
                c+=1
            if(c>2):
                return False
        return True
for _ in range(int(input())):
    s = input()
    if checkgar(s):
        print("yes")
    else:
        print("no")