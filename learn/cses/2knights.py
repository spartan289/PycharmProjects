num = int(input())
for n in range(1,num+1):
    ncr = (n*n)*(n*n-1)//2
    knights =4*(n-1)*(n-2)
    print(ncr-knights)