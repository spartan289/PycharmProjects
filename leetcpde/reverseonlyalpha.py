class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start=0
        end=len(s)-1
        while start<end:
            if s[start].isalpha() and s[end].isalpha():
                s[start], s[end] = s[end], s[start]

                start+=1
                end-=1
            elif s[start].isalpha() and not s[end].isalpha():
                end-=1
            elif  not s[start].isalpha() and s[end].isalpha():
                start+=1
            else:
                start+=1
                end-=1

        return ''.join(s)
s1 = Solution()
print(s1.reverseOnlyLetters("-a-bC-dEf-ghIj"))

        
                


