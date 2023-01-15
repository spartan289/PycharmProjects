def bin_sub(s: str):
    n = len(s)
    dp=[1 for i in range(n+1)]
    # prev=1
    # prev2=0
    mod=998244353
    for i in range(1,n):
        dp[i+1]=dp[i]
        if s[i]!=s[i-1]:
            dp[i+1]+=dp[i-1]

        dp[i+1]%=mod
    print(dp[n])
for _ in range(int(input())):
    bin_sub(input())