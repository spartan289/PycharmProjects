for _ in range(int(input())):
    g=int(input())
    c=0
    for n in range(1,g//2+2):
       k = (2*g+n-n*n)/(2*n)
       if k<=0:
           break
       if k.is_integer():
           c+=1
    print("Case #{}: {}".format(_+1,c))
