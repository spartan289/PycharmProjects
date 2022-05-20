# def check_string(string: str):
#     #check if string contain only letters or alternatively numbers and alphabets adjancent to escj other
#     if len(string)==0:
#         return True
#     elif len(string)==1 and string[0].isdigit():
#         return True
#     if string.isalpha():
#         return False
#     else:
#         for i in range(len(string)):
#             if string[i].isdigit() and i%2!=0:
#                 return True
#             elif string[i].isalpha() and i%2==0:
#                 return True
#         if string[-1].isdigit():
#             return True
#         return False
#
# def translate_String(string : str):
#     if check_string(string):
#         return "VOLDEMORT"
#     ans = ''
#     if string[0].isdigit():
#         for i in range(len(string)):
#             if string[i].isdigit():
#                 ans += int(string[i])* string[i+1]
#     else:
#         ans = ""
#         cnt = (string[0],1)
#         for i in range(1,len(string)):
#             if string[i]==string[i-1]:
#                 cnt = (string[i],cnt[1]+1)
#             else:
#                 ans += (str(cnt[1])+str(cnt[0]))
#                 cnt = (string[i],1)
#         ans += (str(cnt[1])+cnt[0])
#     return ans
# for _ in range(int(input())):
#     print(translate_String(input()))
# # for _ in range(int(input())):
# #     s = set()
# #     n = input()
# #     for i in n:
# #         s.add(n)
# #     print(len(s))
# # #replace last 5 character with 'A'
# # n = input()
# # print(n[:-5]+'A'*5)
# #
# # n,k = map(int,input().split())
# # arr = list(map(int,input().split()))
# # arr.sort()
# # ans = arr[n - 1] - arr[0]
# # tempmin = arr[0]
# # tempmax = arr[n - 1]
# # for i in range(1, n):
# #     tempmin = min(arr[0] + k, arr[i] - k)
# #     tempmax = max(arr[n - 1] - k, arr[i - 1] + k)
# #     ans = min(ans, tempmax - tempmin)
# # print(ans)
#
# # for _ in range(int(input())):
# #     preferences = list(input().split())
# #     li = list(input().split())
# #     ind1 = preferences.index(li[0])
# #     ind2 = preferences.index(li[1])
# #     if ind1 < ind2:
# #         print(preferences[ind1])
# #     else:
# #         print(preferences[ind2])
#
#
# a,b,c,d,e,f=map(int,input().split())
# if a*c*e < b*d*f or  a==0 and b*d>0 or c==0 and d>0:
#     print("Ron")
# else:
#     print("Hermione")
for _ in range(int(input())):
    n,k = map(int,input().split())
    li = []
    for i in range(n):
        a = list(map(int,input().split()))
        li.append(a)
    ans = -1
    for i in li:
        curr = 0
        for j in li:
            if abs(i[1]-j[1])+abs(i[0]-j[0])<=k:
                curr+=1
            if curr==n:
                ans=1
    print(ans)