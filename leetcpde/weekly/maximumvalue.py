def maxValue(n: str, x: int) -> str:
    def listToString(s):
        str1 = ""

        for ele in s:
            str1 += ele
        return str1

    if int(n) >= 0:
        for i in range(len(n)):
            z=n[i]
            if int(z) <x:
                n = list(n)
                n.insert(i, str(x))
                n = listToString(n)
                break
            if i==len(n)-1:
                n = list(n)
                n.append(str(x))
                n = listToString(n)
    else:
        for i in range(1,len(n)):
            z=n[i]
            if int(z) >x:
                n = list(n)
                n.insert(i, str(x))
                n = listToString(n)
                break
            if i==len(n)-1:
                n = list(n)
                n.append(str(x))
                n = listToString(n)

    return n


print(maxValue("73",6))
