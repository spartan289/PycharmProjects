def editDistance(s,t):
    temp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(temp[0])):
        temp[0][i]=i
    for i in range(len(temp)):
        temp[i][0]=i
    for i in temp:
        print(i)
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1]==t[j-1]:
                temp[i][j]=temp[i-1][j-1]
            else:
                temp[i][j] = 1+min(temp[i-1][j-1],temp[i-1][j],temp[i][j-1])
    for i in temp:
        print(i)
    return temp[len(s)][len(t)]
print(editDistance("ecfbefdcfca","badfcbebbf"))