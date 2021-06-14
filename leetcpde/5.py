def ispalindrome(string):
    for i in range(0, len(string) // 2):
        if (string[i] != string[len(string) - i - 1]):
            return False
    return True

def longestPalindrome(s):
    if len(s)==1:
        return s
    maxlen = ""
    curr =""
    for i in range(len(s)):
        for j in range(i,len(s)):
            if ispalindrome(s[i:j+1]):
                curr = s[i:j+1]
                if len(curr)>=len(maxlen):
                    maxlen = curr
    return maxlen
print(longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
                 
             

