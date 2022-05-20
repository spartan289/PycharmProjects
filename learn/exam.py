#print this pattern
#      A
#    B * B
#   C *** C
#  D ***** D
# E ******* E

def displaypattern(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        print(chr(64+i),end="")
        print("*"*(2*(i-1)-1),end="")
        if i!=1:
            print(chr(64+i),end="")
        print()

# Consider the following strings:
#  str1 = “Ronald Brown”
#  str2 = “Richard Brown”
# str3 = “Harry/* Potter% is ^a fictional !! character-&”
# • Write a Python function append_Strings() to create a new string, str4 by appending
# str1 and str2 without using in-built Python functions.
# • Write Python code snippet to arrange the characters of str4 so that all lowercase letters should
# come first. Also, find all the occurrences of substring “row” in str4 ignoring the case; without
# using in-built Python functions.
# • Using an in-built Python function, write a statement to remove all the special symbols from
# str3

def append_Strings(str1,str2):
    str3=str1+str2
    return str3

str1="Ronald Brown"
str2="Richard Brown"
str3=append_Strings(str1,str2)
print(str3)
# • Write Python code snippet to arrange the characters of str4 so that all lowercase letters should
# come first. Also, find all the occurrences of substring “row” in str4 ignoring the case; without
# using in-built Python functions.
a = 'row'
ab  = ''
for i in str3:
    if ord('a')<=ord(i)<=ord('z'):
        ab+=i
for i in str3:
    if not ord('a')<=ord(i)<=ord('z'):
        ab+=i

str3 = ab
print(str3)
str3 = 'Harry/* Potter% is ^a fictional !! character-&'
for i in str3:
    if i.isidentifier():
        print(i,end="")
for i in range(len(str3)):
    if str3[i:i+3]=='row':
        print('Occured at index',i)
