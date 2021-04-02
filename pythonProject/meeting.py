def ist(s):
    time=s[0].split(':')
    if s[1]== 'AM':
        if time[0]== '12':
            final=int(time[1])
        else:
            final=(int(time[0])*100)+int(time[1])
    else:
        if time[0]== '12':
            final=(int(time[0])*100)+int(time[1])
        else:
            final=(int(time[0])*100)+int(time[1])+1200
    return final

t=int(input())

for i in range(t):
   meet = ist(input().split())
   n=int(input())
   l=[]
   for x in range(n):
       s=input().split()
       start=s[0]+' '+s[1]
       end=s[2] +' '+s[3]
       l.append([ist(start.split()),ist(end.split())])
   ans=""
   for x in l:
       if(x[0]<=meet and x[1]>=meet):
           ans+='1'
       else:
           ans+='0'
   print(ans)