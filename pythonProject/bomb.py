t=int(input())
for q in range(t):
    s=input()
    c=0
    for i in s:
        if i=='#':
            c+=1
    print(c)