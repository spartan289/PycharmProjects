from math import sqrt


def powerofsum(x,n):
    li=[]
    for i in range(1,int(sqrt(x))+1):
        li.append(i)
    def findpowersum(li,x,n,index):
        memo={}
        if x==0:
            return 1
        if index>=len(li):
            return 0
        key = x+'-'+index
        if memo.count(key):
            return memo[key]
        ways =findpowersum(li,x,n,index+1)+findpowersum(li,x-pow(li[index],n),n,index+1)
        memo[key]=ways
        return ways
    return findpowersum(li,x,n,0)
x=int(input())
n=int(input())
print(powerofsum(x,n))