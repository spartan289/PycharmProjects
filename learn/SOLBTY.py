for _ in range(int(input())):
    x, a, b = map(int, input().split())
    y = a + (100 - x) * b
    print(y * 10)
