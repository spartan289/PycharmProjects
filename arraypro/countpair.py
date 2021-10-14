def countpair(arr, p, k, n):
    c=0
    arr1 = [i%p for i in arr]
    arr2 = [((i%p)**2)%p for i in arr]
    for i in range(n):
        for j in range(i+1,n):
            formula =(arr2[i]+arr2[j]+(arr1[i])*(arr1[j]))%p
            if formula==k:
                c+=1
    print(c)


for _ in range(int(input())):
    n,k,p = map(int,input().split())
    arr = list(map(int,input().split()))
    countpair(arr, p, k, n)