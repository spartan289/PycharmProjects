s = input()
freq = {}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
is_sol=-1
odd_char=""
for i in freq:
    if freq[i]%2!=0:
        odd_char=i
        is_sol+=1
if is_sol>1 or (is_sol==1 and len(s)%2==0):
    print("NO SOLUTION")
else:
    s=""
    f=""
    sec=""
    for i in freq:
        s = i*(freq[i]//2)
        f=f+s
        sec=s+sec
    print(f+odd_char+sec)