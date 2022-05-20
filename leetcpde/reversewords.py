def reversewords(s:str):
    result = []
    i=0
    x = ''
    while i<len(s):
        if s[i]==' ':
            if len(x)!=0:
                result.append(x)
                x = ''
        else:
            x+=s[i]
        i+=1
    if len(x)!=0:
        result.append(x)
    result.reverse()
    return ' '.join(result)
print(reversewords(s = "  hello world  "))