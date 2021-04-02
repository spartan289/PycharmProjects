number=int(input("enter the number you want to reverse"))
rev=0
while number!=0:
    rem=number%10
    rev=rev*10+rem
    number=number//10
print(rev)