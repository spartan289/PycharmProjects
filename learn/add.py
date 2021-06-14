l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = []
i = 0
carry=0
while i < len(l1):
        if i<len(l2):
            if l1[i]+l2[i]<10:
                l3.append(l1[i]+l2[i]+carry)
                carry = 0
            if l1[i]+l2[i]+carry >=10:
                l3.append(l1[i]+l2[i]+carry-10)
                carry = 1
        if i>=len(l2):
            if carry == 1:
                if l1[i]+carry==10:
                    l3.append(0)
                    carry=1
                else:
                    l3.append(l1[i]+carry)
                    carry = 0
            else:
                l3.append(l1[i])
        i+=1
if carry == 1:
    l3.append(1)
print(l3)







