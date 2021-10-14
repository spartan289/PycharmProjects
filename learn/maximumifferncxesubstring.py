def maxSubstring(S):
    localmax=0
    globalmax = float('-inf')
    for i in range(len(S)):
        if S[i]=='0':
            localmax =max(1,localmax+1)
        else:
            localmax = max(-1,localmax-1)
        globalmax = max(globalmax,localmax)
    return globalmax
print(maxSubstring(S = "0"))
        