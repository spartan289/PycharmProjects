n = int(input())
if n<4 and n>1:
    print("NO SOLUTION")
else:
    li =[0 for i in range(n)]
    odd = 1
    even = 2
    for i in range(n):
        if i<n//2:
            li[i]=even
            even+=2
        else:
            li[i]=odd
            odd+=2

    print(*li)