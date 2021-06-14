
def combination(n):
    c = 1
    for i in range(1,n+2):
        print(int(c%(10**9)),end=" ")
        c = c * (n+1-i)/i
for _ in range(int(input())):
    n=int(input())
    combination(n)
    print()
