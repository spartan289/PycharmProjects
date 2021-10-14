def isInterleave(a,b,c):
    dp = [[False for i in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            l = i+j-1
            if i==0 and j==0:
                dp[i][j]=True

            elif i==0:
                if c[l]==b[j-1]:
                    dp[i][j]=dp[i][j-1]


            elif j==0:
                if a[i-1]==c[l]:
                    dp[i][j]=dp[i-1][j]

            elif a[i-1]==c[l] and b[j-1]!=c[l]:
                dp[i][j]=dp[i-1][j]
            elif a[i-1]!=c[l] and b[j-1]==c[l]:
                dp[i][j]=dp[i][j-1]
            elif a[i-1]==c[l] and b[j-1]==c[l]:
                dp[i][j]= dp[i-1][j] or dp[i][j-1]

    return dp[len(a)][len(b)]
print(isInterleave('XYZ','ABC','XAYBCZ'))



