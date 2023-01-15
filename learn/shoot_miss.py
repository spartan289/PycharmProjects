hh1,mm1 = map(int,input().split())
hh2,mm2 = map(int,input().split())

rem1 = (mm1+mm2)
rem2 = hh1+hh2
if(rem1>59):
    rem2+=1
    rem1-=60
if(rem2>23):
    rem2-=24


print(f"{rem2:02d}",f"{rem1:02d}")