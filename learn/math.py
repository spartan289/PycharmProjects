# 180 degree rotation point
for _ in range(int(input())):
    px,py,qx,qy=map(int,input().split())
    rx=2*qx-px
    ry=2*qy-py
    print(rx,ry)

