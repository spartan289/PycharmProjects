import math
import random
def shuffled_anagram(s):
    for i in range(math.factorial(len(s))):
        temp = list(s)
        random.shuffle(temp)
        temp = ''.join(temp)
        flag=1
        for j in range(len(s)):
            if s[j]==temp[j]:
                flag=0
        if flag:
            return temp
            break
    if not flag:
        return 'IMPOSSIBLE'
for _ in range(int(input())):
    n = input().strip()
    print("Case #{}: {}".format(_+1,shuffled_anagram(n)))


            
