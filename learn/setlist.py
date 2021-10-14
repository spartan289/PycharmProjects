# Writeafunctionthattakesanumber(>=10)asaninputandreturnthedigitsof
# thenumberasaset
def numberset():
    print("Enter the integer : ", end=" ")
    n = int(input())
    s = set(int(x) for x in str(n))
    print("Set", s)


numberset()


def listoperation(li):
    def checklist(li):
        flag = True
        for i in li:
            if not isinstance(i, int):
                flag = False
        return flag

    if checklist(li):
        print("List is of type integer")
        c = 0
        for i in li:
            if i % 2 != 0:
                c += 1
        print("Number of odd Values ", c)
    else:
        print("List is of type String")
        maxlenstr = ''
        currentValue = 0
        for i in li:
            if len(i) > currentValue:
                currentValue = len(i)
                maxlenstr = i
        print("Maximum Element in String is ", maxlenstr)


print()
print()
li1 = [1, 2, 3, 4, 5]
print(li1)
listoperation(li1)
print()
li2 = ['a', 'bc', 'wegas', 'sd', 'wetewsdg']
print(li2)
listoperation(li2)
