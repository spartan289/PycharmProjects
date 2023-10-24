import math


# def g(n):
#     ans = 0
#     for k in range(1, n + 1):
#         ans += k * 10 ** (k - 1)
#     return ans * 9
#
#
# def find_bound(a):
#     up = 0
#     low = 0
#     for i in range(19):
#         if a < g(i):
#             up = i
#             low = i - 1
#             break
#     return up, low
#
# for _ in range(int(input())):
#     a = int(input())
#     up, low = find_bound(a)
#
#     d = g(up)-a
#     r = d%up
#     s = d-r
#     q = s/up
#
#     p = 10**up - 1 - q
#     print(p)
#     print(str(int(p))[-r-1])

def index_position(n,pos):
    i=1
    while n>0:
        tmp = n % 10
        if i==pos:
            return tmp
        n = n//10
        i+=1
    return 0

for _ in range(int(input())):
    n = int(input())
    dig = 1
    curr = 0
    c=1

    while  n> dig*9*c:
        n = n - (dig*9*c)
        dig+=1
        curr = curr*10 + 9
        c*=10
    tmp1 = n//dig
    curr = curr + tmp1
    tmp2 = n%dig

    if tmp2==0:
        print(index_position(curr,1))
    else:
        curr+=1
        print(index_position(curr,dig-tmp2+1))




def num(n,k):
    assertEqual(n,1)