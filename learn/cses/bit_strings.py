n = int(input())
mod = 1e9+7
ans = 1
for i in range(n):
    ans = (ans*2)%mod
ans = ans%mod
print(int(ans))