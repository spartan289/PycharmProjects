def match(s: str,p: str):
    if len(p)<len(s):
        return "IMPOSSIBLE"
    if len(p)==len(s) and p!=s:
        return "IMPOSSIBLE"
    ind = 0
    cnt = 0
    indp = 0
    skip = 0
    while ind<len(s):
        if s[ind]==p[indp]:
            ind+=1
            indp+=1
        else:
            skip+=1
            indp+=1
            cnt+=1
        if len(p)-skip<len(s):
            return "IMPOSSIBLE"
    if s[0:ind+1]==s[0:indp+1]:
        return len(p)-len(s)
    return cnt
for _ in range(int(input())):
    s = input()
    p = input()
    print(f"Case #{_+1}: {match(s, p)}")
