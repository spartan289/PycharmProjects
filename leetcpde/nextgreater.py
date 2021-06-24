# # def next(li):
# #     n = len(li)
# #     for i in range(n):
# #         flag=0
# #         for j in range(i, n):
# #             if li[j] > li[i]:
# #                 li[i] = li[j]
# #                 flag = 1
# #                 break
# #         if flag == 0:
# #             li[i] = 0
# #     return li
# #
# # def largestOddNumber(num: str) -> str:
# #      x = len(num)
# #      for i in range(x-1,-1,-1):
# #          if int(num[i])%2!=0:
# #              return num[0:i+1]
# #      return ""
# #
# # #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
import math
def numberOfRounds(startTime: str, finishTime: str) -> int:
    round = 0
    hs = startTime[0]+startTime[1]
    hs = int(hs)
    ms = startTime[3]+startTime[4]
    ms = int(ms)
    totals = hs*60*60+ms*60
    hf = finishTime[0] + finishTime[1]
    hf = int(hf)
    mf = finishTime[3] + finishTime[4]
    mf = int(mf)
    totalf = hf*60*60+mf*60
    if totalf>totals:
        if totals%900==0 and totalf%900==0:
            round = (totalf-totals)//900
            return (round)
        totals = 900*math.ceil(totals/900)
        totalf = 900*math.floor(totalf/900)
        round = (totalf - totals) // 900
        if round == -1:
            return 0
        return (round)
    if totals>totalf:
        time = 0
        lim =86400

        if totals%900==0:
            round1 = (lim-totals)//900
        if totalf%900==0:
            round2 = (totalf)//900

        totals = 900*math.ceil(totals/900)
        totalf = 900*math.floor(totalf/900)
        round1 = (lim - totals) // 900
        round2 = (totalf) // 900

        return round1+round2
    if totals==totalf:
        return 0
print(numberOfRounds("00:47","00:57"))
# #
#
#
# def findMinDiff(self,qarr, n):
#        diff = 10**20
#        if qarr.length==0:
#            return diff
#        for i in range(len(qarr)):
#            for j in range(i+1,len(qarr)):
#                if qarr[i]!= qarr[j]:
#                    diff =  min(diff,abs(qarr[i]-qarr[j]))
#        if diff == 10**20:
#            return diff
#
#
# def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
#         x = []
#         for query in queries:
#             f = query[0]
#             e = query[1]
#             ans = self.findMinDiff(nums[f:e+1],e-f+1)
#
#             x.append(ans)
#         return x
#
# def FindMaxSum(a, n):
#     first = 0
#     second = 0
#     for i in a:
#         if second>first:
#             sum = second
#         else:
#             sum = first
#
#         first = second+i
#         second = sum
#     if second>first:
#         return second
#     else:
#         return first
#
# print(FindMaxSum([1,2,3],3))
# def findpalindrome(s):
#     n = len(s)
#     if n <= 1:
#         return s
#     ans = None
#     max_len = 1
#     start = 0
#     for i in range(1, n):
#         left = i - 1
#         right = i
#         while (left >= 0) and (right < n) and (s[left] == s[right]):
#
#             l = right - left + 1
#             if l > max_len:
#                 max_len = l
#                 ans = s[left + 1:max_len]
#                 start = left
#
#             left -= 1
#             right += 1
#
#         left = i - 1
#         right = i + 1
#         while (left >= 0) and (right < n) and (s[left] == s[right]):
#
#             l = right - left + 1
#             if l > max_len:
#                 max_len = l
#                 ans = s[left + 1:max_len]
#                 start = left
#             left -= 1
#             right += 1
#     ans = s[start:start + max_len]
#     return ans
# print(findpalindrome("aaaabbaa"))
# def cyclic(i,v,adj,visited,inc):
#     visited[i]=True
#     inc[i]=True
#     for j in range(len(adj[i])):
#         if not visited[adj[i][j]] and cyclic(adj[i][j],v,adj,visited,inc):
#             return True
#         else:
#             if inc[adj[i][j]]:
#                 return True
#     inc[i]=False
#     return False
#
#
#
# def isCyclic(v,adj):
#     visited = [False for i in range(v)]
#     inc = [False for i in range(v)]
#     for i in range(v):
#         if not visited[i]:
#             if cyclic(i,v,adj,visited,inc):
#                 return True
#     return False
#
#
