n=int(input())
for i in range(n):
        for j in range(n-i):
            print('.', end='')
        for k in range(2*i+1):
            print('*',end='')
        for j in range(n-i):
            print('.', end='')
        print()
print("."*n+"*"+"."*n)