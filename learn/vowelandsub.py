
    
def findsub(s, k):
        # Write your code here
        vowels = "aeiou"
        start = 0
        maxVowels = maxLen = 0
        vowel_count = 0
        st = 'Not found!'
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_count += 1
            if i - start + 1 - maxVowels > k:
                if s[start] in vowels:
                    vowel_count -= 1
                start += 1
            if  vowel_count>maxLen:
                maxLen = vowel_count
                st = s[start:start + k]
        return st  
print(findsub('azerdii',5))