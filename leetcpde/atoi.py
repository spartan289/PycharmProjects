# Soumya Shrestha <soumya2.shrestha@aricent.com>
def myAtoi(s: str) -> int:
    if not s or not s.replace(" ", ""):
        return 0
    s = s.strip()
    converted = ""
    sign = ""
    if s[0] == "+" or s[0] == "-":
        sign = s[0]
        s = s[1:]
    for i in s:
        if i.isnumeric():
            converted += i
        else:
            break

    if converted:
        if sign == "-":
            converted = 0 - int(converted)
        converted = int(converted)
        if converted < -2147483648:
            return -2147483648
        elif converted > 2147483647:
            return 2147483647
        else:
            return converted
    else:
        return 0


print(myAtoi("-0020023"))