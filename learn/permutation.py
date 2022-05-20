def uniqueperm(arr,n):
    result = []
    def recursion(x, y,result):
        if y == 3:
            return x
        else:
            ans = []
            for i in range(y, len(x)):
                x[i], x[y] = x[y], x[i]
                ans += recursion(x, y + 1, result)
                x[i], x[y] = x[y], x[i]
    recursion(li,0,result)
    print(result)
    print(len(result))
from itertools import permutations
def uniquepermutation(arr,n):
    return set(permutations(arr))
li = [1, 2, 3]
# recursion(li,0)
print(uniquepermutation([2, 1, 2, 3, 4, 5],4))