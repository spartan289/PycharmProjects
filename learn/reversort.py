def reversort(l):
    def reverse(seq, start, stop):
        size = stop + start
        for i in range(start, (size + 1) // 2):
            j = size - i
            seq[i], seq[j] = seq[j], seq[i]
        return seq
        
    cost=0
    for i in range(len(l)-1):
        j=min(l[i:len(l)])
        j=l.index(j)
        reverse(l,i,j)
        sum=(j)-(i)+1
        cost+=sum
    return cost
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=reversort(l)
    print("Case #{}: {}".format(_+1,c))
    