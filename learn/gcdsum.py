def gcd(a, b):
    return a if (b == 0) else gcd(b, a % b)


for _ in range(int(input())):
    k = int(input())
    arr1=[]
    for i in range(1, (2 * k) + 2):
        arr1.append(k+(i**2))
    arr2=[]
    for j in range(len(arr1)-1):
        arr2.append(gcd(arr1[j],arr1[j+1]))

    print(sum(arr2))
