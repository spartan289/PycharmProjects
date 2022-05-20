def calc(arr):
    c = 0
    if ((arr[0][1] - arr[0][0]) == (arr[0][2] - arr[0][1])):
        c += 1
    if ((arr[1][1] - arr[1][0]) == (arr[1][2] - arr[1][1])):
        c += 1
    if ((arr[2][1] - arr[2][0]) == (arr[2][2] - arr[2][1])):
        c += 1
    if ((arr[1][0] - arr[0][0]) == (arr[2][0] - arr[1][0])):
        c += 1
    if ((arr[1][1] - arr[0][1]) == (arr[2][1] - arr[1][1])):
        c += 1
    if ((arr[1][2] - arr[0][2]) == (arr[2][2] - arr[1][2])):
        c += 1

    if ((arr[1][1] - arr[0][0]) == (arr[2][2] - arr[1][1])):
        c += 1
    if ((arr[1][1] - arr[0][2]) == (arr[2][0] - arr[1][1])):
        c += 1
    return c


for _ in range(int(input())):
    a = list(map(int, input().split()))
    b1, b3 = map(int, input().split())
    c = list(map(int, input().split()))
    arr = []
    arr.append(a)
    arr.append([b1, 0, b3])
    arr.append(c)
    ans = 0
    if (arr[1][0] + arr[1][2])%2==0:
        arr[1][1] = (arr[1][0] + arr[1][2]) // 2
        cp = calc(arr)
        ans = max(ans,cp)
    if (arr[0][0] + arr[2][2])%2==0:
        arr[1][1] = (arr[0][0] + arr[2][2]) // 2
        cp = calc(arr)
        ans = max(ans,cp)
    if (arr[0][2] + arr[2][0])%2==0:
        arr[1][1] = (arr[0][2] + arr[2][0]) // 2
        cp = calc(arr)
        ans = max(ans,cp)
    if (arr[0][1] + arr[2][1])%2==0:
        arr[1][1] = (arr[0][1] + arr[2][1]) // 2
        cp = calc(arr)
        ans = max(ans,cp)
    print("Case #{}: {}".format(_ + 1, ans))
