for _ in range(int(input())):
    x,y,a,b,k = map(int,input().split())
    k+=1
    x+=k*a
    y+=k*b
    if x>y:
        print("DIESEL")
    elif x<y:
        print("PETROL")
    else:
        print("SAHILLSWME PRICE")