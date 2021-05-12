def appendatFront(x, L):
    return [x+element for element in L]
def bitstring(n):
    if n==0:
        return []
    if n==1:
        return ["0","1"]
    else:
        return appendatFront("0",bitstring(n-1))+appendatFront("1",bitstring(n-1))
print(bitstring(3))