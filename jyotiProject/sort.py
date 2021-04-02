
#using the built-in sorted function to sort data content

testScore=[82,34,55,66,87,89,32,31,45,65]

#perform a simple sort using sorted
sortedScore=sorted(testScore)
print(sortedScore)
#explicitly declare a sort order- ascending and descending
sortedScores=sorted(testScore,reverse=True)
print(sortedScores)
