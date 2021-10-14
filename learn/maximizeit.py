n,k = map(int,input().split())

lists = [list(map(int,input().split())) for i in range(n)]
arr = []

from itertools import product
results = map(lambda x: sum(i**2 for i in x)%k, product(*lists))
print(max(results))

