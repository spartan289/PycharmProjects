def isAnagram(a,b):
    mapa = {}
    mapb = {}
    for i in a:
        if i in mapa:
            mapa[i]+=1
        else:
            mapa[i]=1
    for i in b:
        if i in mapb:
            mapb[i]+=1
        else:
            mapb[i]=1
    for i in mapa:
        if i in mapb and mapa[i]==mapb[i]:
            continue
        else:
            return False
    for i in mapb:
        if i in mapa and mapb[i]==mapa[i]:
            continue
        else:
            return False
    return True
print(isAnagram(a="allergy", b="allergic"))