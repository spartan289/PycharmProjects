#chefreci
# for _ in range(int(input())):
#     n=int(input())
#     n=2*pow(n,2)+pow(-1,n)-1
#     an=n//4
#     print(int(an))
def sumofposition(li):
    soe=0
    soo=0
    for i in range(len(li)):
        if i%2==0:
            soo+=li[i]
        else:
            soe+=li[i]
    if soo==soe:
        return True
    else:
        return False

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    for i in li:
        x=li.index(i)

        li.remove(i)

        if(sumofposition(li) is True):
            print(i)
            break
        else:
            li.insert(x,i)




