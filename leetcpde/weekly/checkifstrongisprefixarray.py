def isPrefixString(s: str, words: list[str]) -> bool:

    # c=0
    # for i in range(len(s)):
    #     for j in range(i,len(s)):
    #         if s[i:j+1] in words:
    #             c+=1
    # if c==len(s):
    #     return True
    # else:
    #     return False
    # c=0
    # for word in words:
    #
    #     if word in s:
    #         c+=len(word)
    #     if c == len(s):
    #             return True
    #     if word not in s:
    #         return False
    j=0


    x=""
    while j<len(words):
        x += words[j]
        if x == s:
            return True
        j+=1
    return False


print(isPrefixString(s = "z", words = ["z"]))