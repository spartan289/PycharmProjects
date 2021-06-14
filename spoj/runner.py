if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(n - 1):
        if arr[i + 1] == arr[i]:
            continue
        else:
            print(arr[i])
            break
