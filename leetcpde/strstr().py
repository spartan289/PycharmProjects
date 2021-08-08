def strstr(haystack,needle):
    if len(haystack)==0 :
        return 0
    if len(needle)>len(haystack):
        return 0
    n = len(needle)
    for i in range(len(haystack)):
        p = haystack[i:i+n]
        if p==needle:
            return i
    return -1
print(strstr("","a"))
