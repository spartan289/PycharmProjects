from itertools import permutations
l = list(permutations([1,2,3]))
li = []
for i in l:
    li.append(list(i))
print(li)
