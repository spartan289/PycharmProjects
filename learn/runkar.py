t=int(input(""))
while(t>0):
    q=o=z=0
    n=int(input(""))
    str=input("")
    i=0
    for i in range(len(str)):
        if(str[i]=="?"):
            q+=1
        elif(str[i]=="1"):
            o+=1
        elif(str[i]=="0"):
            z+=1
        i+=1
    while(q>0):
        if(z>o):
            str=str.replace("?","1")
            z-=1
            o+=1
        elif(z==o):
            str=str.replace("?","1")
            z-=1
            o+=1
        elif(z<0):
            str=str.replace("?","0")
            o-=1
            z+=1
        q-=1
    print(str)
    t-=1