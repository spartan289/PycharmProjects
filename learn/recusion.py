def recmeth(n):
    if n<1:
        print("n is less than 1")
    else:
        recmeth(n-1)
        print(n)
recmeth(4)