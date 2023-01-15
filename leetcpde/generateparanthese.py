def isBalanced(s):
    hashmap = {")":"("}
    stack = []
    for i in s:
        if i in hashmap:
            if len(stack)==0:
                return False
            top_element = stack.pop()
            if hashmap[i]!=top_element:
                return False
        else:
            stack.append(i)
    return True if len(stack)==0 else False
def permutation(x,y,n,s):

    if y==n-1:
        if x.copy() not in s:
            if isBalanced(x):
                s.append(x.copy())
    else:
        for i in range(y,n):
            x[i],x[y] = x[y],x[i]
            if(x.copy() not in s):
                permutation(x,y+1,n,s)
            x[i],x[y] = x[y],x[i]
def generate_paranthese(n):
    par=[]
    for i in range(n):
        par.append('(')
    for j in range(n):
        par.append(')')
    s = []
    permutation(par,0,n*2,s)
    for i in range(len(s)):
        s[i]=''.join(s[i])
    return s
print(generate_paranthese(8))


