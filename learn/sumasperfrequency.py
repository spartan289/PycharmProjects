n = int(input())
arr = list(map(int,input().split()))
hash = {}
for i in arr:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1
new_dict = {}

for key, value in hash.items():
   if value in new_dict:
       new_dict[value] += key
   else:
       new_dict[value]=key
for _ in range(int(input())):
    sum=0
    l,r = map(int,input().split())
    a=0
    for i in range(l,r+1):
        if i in new_dict:
                sum+=new_dict[i]*i
    print(sum)

