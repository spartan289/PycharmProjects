def reverseWords(s):
        # code here
        n = len(s)
        prev=0
        res = ''

        for i in range(n):
            if s[i]=='.'or i==n-1:
                if i==n-1:
                    res += s[prev:i+1][::-1]
                else:
                    string = s[prev:i]
                    string = string[::-1]
                    res+=string
                    if i!=n-1:
                        res+='.'

                    prev=i+1
        return res
print(reverseWords(s = 'pqr.mno'))
