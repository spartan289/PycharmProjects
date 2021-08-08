def groupAnagrams(strs: list[str]) -> list[list[str]]:
    for i in strs:
        for j in i:
            x+=ord(j)