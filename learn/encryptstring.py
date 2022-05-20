def encryptString(s):
    # code here
    n = len(s)
    ans = ''
    i=0
    while i<n:
        curr = s[i]
        count=0
        while s[i]==curr:
            count+=1
            i+=1
            if i==n:
                break
        ans+=curr
        i-=1
        ans+=hex(count)[2:][::-1]
        i+=1
    return ans[::-1]
n=input()
print(encryptString(n))