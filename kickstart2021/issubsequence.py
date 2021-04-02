str1=input()
for k in range(int(input())):
    str2=input()
    m=len(str2)
    n=len(str1)
    i=0
    j=0
    while j<m and i<n:
        if str2[j]==str1[i]:
            j+=1
        i+=1
    if j==m:
        print("POSITIVE")
    else:
        print("NEGATIVE")