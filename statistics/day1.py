def mean(n,arr):
    x=sum(arr)/n
    x = "{:.2f}".format(x)
    print(x)
def median(n,arr):
    if n%2==0:
        x=arr[n//2]+arr[(n+1)//2]
        x=x/2
        x = "{:.2f}".format(x)
        print(x)
def mod(n,arr):
    max=0
    count=0
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            count+=1
        else:
            max = count
            count = 0
    print(max)
n=int(input())
