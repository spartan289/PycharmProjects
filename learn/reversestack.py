stack = list(map(int, input().split()))
temp = []
index = 0
for index in range(len(stack)):
    a = stack.pop()
    while len(stack)!=index:
        temp.append(stack.pop())
    stack.append(a)
    while len(temp)!=0:
        stack.append(temp.pop())
print(stack)



