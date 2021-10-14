def countoccurence(pat,txt):
    pat = list(k for k in pat)
    txt = list(j for j in txt)
    m = len(pat)
    pat.sort()
    c=0
    for i in range(len(txt)-m+1):
        pattxt = txt[i:i+m]
        pattxt.sort()
        if pattxt==pat:
            c+=1
    return c
countoccurence("aaba","aabaabaa")
