#use standard library function to search strings for content

sampleStr="the quick brown fox jump over the lazy dog"

#startswith and endswith functions
print(sampleStr.startswith("the"))
print(sampleStr.startswith("The"))
print(sampleStr.endswith("dog"))

#the find(find from left side) and rfind(find from right side) functions
print(sampleStr.find("the"))
print(sampleStr.rfind("the"))
print("the" in sampleStr)
#using replace
newStr=sampleStr.replace("lazy","tired")
print(newStr)


#counting instances of substrings
#it counts no. of times the word occur
print(sampleStr.count("over"))

