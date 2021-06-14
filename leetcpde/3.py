def longestsubstring(s):
    if len(s) <= 1:
        return len(s)

    m = 0
    window = 1
    i = 0
    while (i + window) <= len(s):
        if len(s[i:i + window]) == len(set(s[i:i + window])):
            m = window
            window += 1
        else:
            i += 1

    return m
print(longestsubstring("abcabcbb"))