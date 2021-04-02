t=int(input())
for _ in range(t):
    n=int(input())
    x=1
    c=1 # vaibhav #c=2anjali
    while n>0:
        if x&n == 0:
            n=n-x
            c+=1
        x += 1

    if c%2==0:
        print("Vaibhavi")
    else:
        print("Anjali")