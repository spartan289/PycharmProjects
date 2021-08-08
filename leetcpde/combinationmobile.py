def comb(x):
    hash = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    li=[]
    if len(x)==2:
        a=hash[int(x[0])]
        b=hash[int(x[1])]
        for i in a:
            for j in b:
                li.append(i+j)
    elif len(x)==3:
        a=hash[int(x[0])]
        b=hash[int(x[1])]
        c = hash[int(x[2])]
        for i in a:
            for j in b:
                for k in c:
                    li.append(i+j+k)
    else:
        a=hash[int(x[0])]
        b=hash[int(x[1])]
        c = hash[int(x[2])]
        d = hash[int(x[3])]
        for i in a:
            for j in b:
                for k in c:
                    for l in d:
                        li.append(i+j+k+l)
    return li
print(comb("235"))