def repition(s):
    c=0
    maxi = 0
    hsh = {
        'A':0,
        'C':0,
        'G':0,
        'T':0,
    }
    for i in range(len(s)):
        if s[i]=='A':
            c+=1
            if i==len(s)-1 and s[i]=='A':
                hsh['A'] = c
                break
            if s[i+1]!='A':
                if hsh['A']<c:
                    hsh['A']=c
                c=0
        if s[i]=='C':
            c+=1
            if i==len(s)-1 and s[i]=='C':
                hsh['C'] = c
                break
            if s[i+1]!='C':
                if hsh['C']<c:
                    hsh['C']=c
                c=0
        if s[i]=='G':
            c+=1
            if i==len(s)-1 and s[i]=='G':
                hsh['G'] = c
                break
            if s[i+1]!='G':
                if hsh['G']<c:
                    hsh['G']=c
                c=0

        if s[i]=='T':
            c+=1
            if i==len(s)-1 and s[i]=='T':

                hsh['T'] = c
                break
            if s[i+1]!='T':
                if hsh['T'] < c:
                    hsh['T'] = c
                c=0



    return max(hsh.values())
s=input()
print(repition(s))



