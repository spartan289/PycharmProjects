
for _ in range(int(input())):
    minicount = 10**9+1

    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    for p in range(n):
        count = 0
        for i in range(n):
            if p!=i:
                eq1 = x[i]-x[p]-y[i]+y[p]
                eq2 = x[i]-x[p]+y[i]-y[p]

                if x[i]==x[p] and y[i]==y[p]:
                     count += 0
                elif x[i]==x[p] or y[i]==y[p]:
                    count+=1
                elif eq1==0 or eq2 == 0:
                    count+=1
                else:
                    count += 2
        minicount = min(minicount,count)
    print(minicount)
