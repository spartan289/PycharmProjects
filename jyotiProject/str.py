import string


print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

test_string1="the quick brown fox"
test_string2="supercalifraligistic"
test_string3="90120"
#python comprehension
result="".join([c for c in test_string1 if c in string.ascii_letters])
print(result)
#check alphanumeric
print(test_string1.isalnum())
print(test_string2.isalnum())

print(all([c.isalpha() for c in test_string2]))

print(test_string3.isnumeric())

