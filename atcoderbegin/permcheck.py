# n = int(input())
# a = list(map(int,input().split()))
# x = [i for i in range(1,n+1)]
# a.sort()
# 
# if a==x:
#     print("Yes")
# else:
#     print("No")
import math
a,b,c = map(int,input().split())

if a>0 and b>0:
    if a>b:
        print('>')
    elif a<b:
        print('<')
    else:
        print('=')
elif a>0 and b<0:
    if c%2==0:
        if a>abs(b):
            print('>')
        elif a<abs(b):
            print('<')
        else:
            print('=')
    else:
        print('>')
elif a<0 and b>0:
    if c%2==0:
        if abs(a)<b:
            print('<')
        elif abs(a)>b:
            print('>')
        else:
            print('=')
    else:
        print('<')
else:
  if c%2==0:
    if abs(a)>abs(b):
      print('>')
    elif abs(a)<abs(b):
      print('<')
    else:
      print('=')
  else:
    if a<b:
      print('<')
    elif a>b:
      print('>')
    else:
      print('=')