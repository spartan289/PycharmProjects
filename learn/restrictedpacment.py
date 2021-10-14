import math
def candies(m, n):
    x = m*n - (m+n)
    c=0
    queue = []
    set = {x}
    queue.append(x)
    while(len(queue)!=0):
        current = queue.pop(0)
        c+=1
        k = current - m
        if(k>0 and k not in set):
            queue.append(k)
            set.add(k)
        k = current - n
        if(k>0 and k not in set):
            queue.append(k)
            set.add(k)
    print(c)

candies(3,11)