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
def longestValidParentheses(s: str) -> int:
    stack = []
    maxi = 0
    hashmap = {")":"("}
    c=0
    i=0
    j=len(s)-1
    while i<j:
        x = s[i:j+1]
        if isBalanced(x):
            c = len(x)
            maxi = max(c,maxi)
            c=0
        i+=1

    return maxi



print(longestValidParentheses("(()"))

