def new_password(n,s):
    upf = False
    lowf = False
    digf = False
    sp = False
    character = ['#', '@', '*', '&']
    for i in range(n):
        if(s[i].isupper()):
            upf = True
        elif(s[i].islower()):
            lowf = True
        elif(s[i].isdigit()):
            digf = True
        elif(s[i] in character):
            sp = True
    if (not upf):
        s += 'A'
    if (not lowf):
        s += 'a'
    if (not digf):
        s += '1'
    if (not sp):
        s += '#'
    while len(s) < 7:
        s += '1'
    return s

for _ in range(int(input())):
    n = int(input())
    s = input()
    print("Case #{}: {}".format(_+1,new_password(n,s)))