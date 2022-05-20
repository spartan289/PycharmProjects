def longestCommonPrefix(str1, str2):
    # code here
    li=[-1,-1]

    for i in range(len(str1)):
        if str1[0:(i + 1)] in str2:
            li=[0,i]
    return li
print(longestCommonPrefix(str1 = "practicegeeks",
str2 = "coderpractice"))