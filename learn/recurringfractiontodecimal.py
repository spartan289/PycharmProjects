def fractiontodecimal(num,den):
    res = ""
    mp = {}
    rem = num%den
    x = rem
    while ((rem!=0) and  (rem not in mp)):
        mp[rem]=len(res)
        rem = rem*10
        res_part = rem// den
        res += str(res_part)
        rem = rem%den
    if rem==0:
        return x,""
    else:
        return x,res[mp[rem]:]
num =int(input())
den = int(input())
x , rem = fractiontodecimal(num,den)
if num%den==0:
    print(num//den)
else:
    st = str(num//den)+'.'+str(x)+'({})'.format(rem)
    print(st)

