def isPalindrome(x: int) -> bool:
    y = str(x)[::-1]
    if x == y:
        return True
    else:
        return False
print(isPalindrome(121))