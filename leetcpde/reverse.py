def reverse(x):
    flag = 0
    if x < 0:
        flag = 1
        x = x * (-1)
    x = str(x)
    x = x[::-1]
    if flag == 1:
        x = '-' + x
    return int(x)


print(reverse(1534236469))