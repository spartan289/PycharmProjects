# def gcd(a, b):
#     # Everything divides 0
#     if (b == 0):
#         return a
#     return gcd(b, a % b)
# print(gcd(1,1))
# from matplotlib import pyplot as plt
# def specialnumcount(nums):
#     """
#     This function counts the number of special numbers in a given range.
#     """
#     count = 0
#     l = []
#
#     for num in range(1,nums+1):
#         x = num
#         sumofquarticpower = 0
#         productofdights = 1
#         while x!=0:
#             digit = x%10
#             sumofquarticpower += digit**4
#             productofdights *= digit
#             x = x//10
#         if gcd(sumofquarticpower, productofdights) >1:
#             l.append(num)
#             count += 1
#             plt.plot(num, count,  'ro')
#     return count,nums
# for i in range(1,100):
#     print(specialnumcount(i))
# There are ‘N’ smartphones with distinct prices. There is also an integer assigned to each phone representing its quality (quality[i] > quality[j] implies phone ‘i’ has better quality than phone ‘j’). The quality of each phone is distinct too.
# Your friend is sure that a higher price definitely means better quality, but you disagree, as you can name quite a few companies that overprice average phones. To settle this debate, your friend asks you to show two phones such that the price of one is lesser than the other, but the quality is higher.
# Print “YES” if a pair of such phones exist, or “NO” otherwise.
#
# def isPairPresent(n: int, cost: list[int], quality: list[int])-> str:
#
#     for i in range(n):
#         for j in range(n):
#             if i!=j and cost[i]<cost[j] and quality[i]>quality[j]:
#                 return "YES"
#     return "NO"
def maxSum(a: list[int], k: int) -> int:
    dp = [0] * (len(a)+1)
    prefix_sum = [None] * (len(a)+1)
    prefix_sum[0] = 0
    for i in range(1, len(a)+1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]
    dp[0] = 0
    for i in range(1,k):
        dp[i] = prefix_sum[i]
    for i in range(k, len(a)+1):

        for j in range(i,i-k,-1):
            dp[i] = max(dp[i],dp[j-1]+prefix_sum[i]-prefix_sum[j])
    return dp[len(a)]

for _ in range(int(input())):
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    print(maxSum(a, k))
