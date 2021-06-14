def covert(word):
    x = ''
    for i in range(len(word)):
        y = ord(word[i]) - ord('a')
        x += str(y)
    x = int(x)
    return x
def isSumEqual(firstWord: str, secondWord: str, targetWord: str):
    firstWord = covert(firstWord)
    secondWord = covert(secondWord)
    targetWord = covert(targetWord)
    if firstWord+secondWord==targetWord:
        return True
    else:
        return False

print(isSumEqual('acb','cba','cdb'))