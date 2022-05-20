
def convert(n: int):
    digit2add = 9 - n%9
    n = list(str(n))
    lenn = len(n)
    position = lenn+1
    if digit2add==9:
        n.insert(1,'0')
    else:
        for i in range(lenn-1,-1,-1):
            if ord(n[i])-ord('0')>digit2add:
                position=i
        c = chr(digit2add+ord('0'))
        n.insert(position, c)
    return ''.join(n)

for _ in range(int(input())):
    n = int(input())
    print(f"Case #{_+1}: {convert(n)}")