def binary(n):
    if n==0:
        print(1,end='')
    binary(int(n/2))
    print(n%2,end='')

print(binary(31))
