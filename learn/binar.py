def countTotalBits(num):
    binary = bin(num)[2:]
    return len(binary)
def multiply(num):
    return int(bin(num)[2:]*10)
def complement(num):
    return ~num
s,e=[int(x,2) for x in input().split()]
c=0
while(s!=e):
    if s==e:
        break
    if countTotalBits(s)>countTotalBits(e):
        s=complement(s)
    else:
        s=multiply(s)

    c+=1




