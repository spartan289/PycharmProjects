def q1():
    a = (1,2,3)
    return
def q2():
    a = (1,'a',3,4.5,True)
def q3():
    a = (1,2,3,4,5)
    print(a[1])
def q4():
    a = (1,2,3,4)
    a = list(a)
    a.append(5)
    a = tuple(a)
    print(a)
def q5():
    a={'a','b','c'}
    x = ''
    for i in a:
        x+=a
    print(x)
def q6():
    a = (1,2,3,4,5,6,7,8,9)
    print(a[3], a[len(a)-4])

def q7():
    a = (1,2,3,4,2,5,6,7,8)
    hash = {}
    for i in a:
        if i in hash:
            print(hash[i])
            hash[i]+=1
        else:
            hash[i]=1

def q8():
    x = 2
    a = (1,2,3,4,5,6,7,8,9)
    if x in a:
        print(True)
    else:
        print(False)

def q9():
    a = (1,2,3,4)
    a = list(a)
    a.reverse()
    a = tuple(a)
    print(a)
def q10():
    a = (1,2,3)
    print("This is a tuple created {}".format(a))
def q11():
    a = ((),(),(2,3),(4,5))
    a = list(a)
    i=0
    while i!=len(a):
        if len(a[i])==0:
            del a[i]
        else:
            i+=1
    a = tuple(a)
    print(a)

