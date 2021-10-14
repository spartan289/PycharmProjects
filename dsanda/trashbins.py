# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     stack = []
#     sum_d = 0
#     arr = []
#     for i in range(n):
#         if s[i]=='1':
#             i+=1
#     k= -1
#     if int(s)!=0:
#         for i in range(n):
#             if s[i]=='1':
#                 stack.append(i)
#             else:
#                 if len(stack)==0:
#                     if k>i:
#                         pr = abs(k - i)
#                     else:
#                         for j in range(i + 1, n):
#                             if s[j] == '1':
#                                 k = j
#                                 break
#                     pr = abs(k-i)
#                     sum_d+=pr
#
#                 else:
#                     x=stack[-1]
#                     p = abs(x-i)
#                     if k>i:
#                         pr = abs(k-i)
#                     else:
#                         for j in range(i+1,n):
#                             if s[j]=='1':
#                                 k=j
#                                 break
#                         pr = abs(k-i)
#                     if pr<p:
#                         sum_d+=pr
#                     else:
#                         sum_d+=p
#     print("Case #{}: {}".format(_+1,sum_d))
#
for _ in range(int(input())):
    n = int(input())
    s = input()
    stack = []
    sum_d = 0
    arr = []
    for j in range(n):
        if s[j]=='1':
            arr.append(j)
    c=0
    if int(s)!=0:
        for i in range(n):
            if s[i]=='1':
                stack.append(i)
                c+=1
            else:

                if len(stack)==0:
                        secondind = arr[c]
                        pr = abs(i-secondind)
                        sum_d+=pr

                else:
                    secondind = arr[c]
                    x = stack[-1]
                    p = abs(x-i)
                    pr = abs(i-secondind)
                    if p>pr:
                        sum_d+=pr
                    else:
                        sum_d+=p

    print("Case #{}: {}".format(_ + 1, sum_d))