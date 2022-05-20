def luckynum():
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        if a==7 or b==7 or c == 7:
            print("YES")
        else:
            print("NO")
# luckynum()
def testseries():
    for _ in range(int(input())):
        li = list(map(int,input().split()))
        india=e=0
        for i in range(5):
            if li[i]==1:
                india+=1
            elif li[i]==2:
                e+=1
        if india>e:
            print("INDIA")
        elif e>india:
            print("ENGLAND")
        else:
            print("DRAW")
testseries()