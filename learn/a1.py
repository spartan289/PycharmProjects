# def connie(s):
#     vowel = ['A','E','I','O','U']
#     flag=0
#     c=0
#     hash = {}
#
#     for i in s:
#         if i in hash:
#             hash[i]+=1
#         else:
#             hash[i]=1
#         if i in vowel:
#             c+=1
#             flag=1
#     if hash[s[0]]==len(s):
#         time=0
#     else:
#         if c==len(s) or c==0:
#
#         if c<len(s)-c:
#             #length of vowel is greater
#
#             max_count = 0
#             max_consonant = ''
#             for i in hash:
#                 if i not in vowel:
#                     if max_count < hash[i]:
#                         max_consonant = i
#                         max_count = hash[i]
#             time = c+(len(s)-c)*2-2*max_count
#         else:
#             max_count = 0
#             max_consonant = ''
#             for i in hash:
#                 if i in vowel:
#                     if max_count < hash[i]:
#                         max_consonant = i
#                         max_count = hash[i]
#             time = c*2+(len(s)-c)-2*max_count
#     print(time)
# for _ in range(int(input())):
#     s = input()
#     connie(s)