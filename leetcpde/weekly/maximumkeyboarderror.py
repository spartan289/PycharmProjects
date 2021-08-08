def canBeTypedWords(text: str, brokenLetters: str) -> int:
    text = list(text.split())
    c = 0
    for i in range(len(text)):
        for j in brokenLetters:
            if j in text[i]:
                c+=1
                break
    return len(text)-c

print(canBeTypedWords("leet code","e"))
