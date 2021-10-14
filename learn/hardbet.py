for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a==min(a,b,c):
        print("Draw")
    elif b == min(a,b,c):
        print("Bob")
    else:
        print("Alice")
