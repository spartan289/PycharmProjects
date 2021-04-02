try:
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(len(arr)):

        fi=min(arr)
        print(len(arr))
        for j in range(len(arr)):
            arr[j]=arr[j]-fi
        arr = [k for k in arr if k != 0]
except :
    print('')


