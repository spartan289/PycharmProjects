def isBalanced(s):
    hashmap = {")":"(","}":"{","]":"["}
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
for _ in range(int(input())):
    s = input()
    print(isBalanced(s))