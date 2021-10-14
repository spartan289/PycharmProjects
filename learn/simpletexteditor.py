import time
string = ''
stack = []
x = time.time()
for _ in range(int(input())):
    query = input()
    if query[0]=='1': #append the string
        stack.append(string)
        string += query[2:]

    elif query[0]=='2':
        stack.append(string)
        string = string[:len(string)-int(query[2:])]

    elif query[0]=='3':
        print(string[int(query[2:])-1])
    elif query[0]=='4':
        string = stack.pop()

print(time.time()-x)
