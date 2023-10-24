n = int(input())
for i in range(2**n):
    print("0"*(n-len(bin(i^(i//2))[2:]))+bin(i^(i//2))[2:])
