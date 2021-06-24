def romanToInt(s: str) -> int:
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dict2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    c = 0
    i = 0
    flag = 0
    while i < (len(s) - 1):
        if (s[i] + s[i + 1]) in dict2:
            c = c + dict2[s[i] + s[i + 1]]
            if i==len(s)-2:
                flag=1

            i += 1
        else:
            c += dict[s[i]]
        i += 1
    if flag!=1:
        if s[i] in dict:
            c += dict[s[i]]
    return c
print(romanToInt("MCMXCIV"))
