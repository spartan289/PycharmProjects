import math


def ispalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
def countpalindrome(n):
    i=1
    count=0
    while i<=math.sqrt(n):
        if n%i==0:
            if(n//i==i):
                if(ispalindrome(str(i))):
                    count+=1
            else:
                if(ispalindrome(str(i))):
                    count+=1
                if(ispalindrome(str(n//i))):
                    count+=1
        i+=1
    # for i in range(1,n):
    #     if ispalindrome(str(i)):
    #         count+=1
    return count
for _ in range(int(input())):
    n=int(input())
    print("Case #{}: {}".format(_+1,countpalindrome(n)))