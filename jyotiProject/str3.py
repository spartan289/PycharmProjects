test_string1="the quick brown fox jumps over the lazy dog on the ist of december"
#upper and lower convert between cases
print(test_string1.upper())

#use the split(split the whole sentence into words) and join(join the words into single line) functions
result=test_string1.split(" ")
print(result)
letters=["the","quick","brown"]
print(",".join(letters))
#use justification functions to align strings
#ljust,center,rjust
names=["amy","john","jyoti","micda"]
big=max(len(name) for name in names)
for name in names:
    print(name.ljust(big+2,"-")+":")
for name in names:
    print(name.center(big+2,"-")+":")
for name in names:
    print(name.rjust(big+2,"-")+":")

#use a translation table to replace characters
sample="the quick brown fox"
trans_table=str.maketrans("abcdefghij","2345532134")
print(sample)
print(sample.translate(trans_table))