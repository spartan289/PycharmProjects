def shuffled_card(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum/n
for _ in range(int(input())):
    n = int(input())
    print("Case #{}: {}".format(_+1,shuffled_card(n)))
