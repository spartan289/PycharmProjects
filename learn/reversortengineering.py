from itertools import permutations


def reversort(l):
    def reverse(seq, start, stop):
        size = stop + start
        for i in range(start, (size + 1) // 2):
            j = size - i
            seq[i], seq[j] = seq[j], seq[i]
        return seq

    cost = 0
    for i in range(len(l) - 1):
        j = min(l[i:len(l)])
        j = l.index(j)
        reverse(l, i, j)
        sum = (j) - (i) + 1
        cost += sum
    return cost
for _ in range(int(input())):

    n,c=map(int,input().split())
    l=list(i for i in range(1,n+1))
    comb = permutations(l)
    flag=0
    for li in list(comb):
        if reversort(list(li))==c:
            print("Case #{}: ".format(_+1),end="")
            for i in li:
                print(i,end=" ")
            print()
            flag=1
            break
    if flag==0:
        print("Case #{}: IMPOSSIBLE".format(_+1,))
