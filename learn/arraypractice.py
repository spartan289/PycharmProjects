from array import *
#1. Create an array and traverse
myarray = array('i',[1,2,3,4,5])
for i in myarray:
    print(i)

#2. Access individual element through indexes
print(myarray[3])
#3. Append any value using append method
print("Step 3")
myarray.append(6)
print(myarray)

#4. insert value in an array using insert() method

print("Step 4")
myarray.insert(6,7)
print(myarray)

#5. Extend python array using extend() method
print("Step 5")
myarray1=array('i',[10,11,12])
myarray.extend(myarray1)
print(myarray)

#6. Add item from list into array using fromlist() method
print("Step 6")
tempList=[8,9]
myarray.fromlist(tempList)
print(myarray)
#7. remove an elemnt from the list using remove() method
print("Step 7")
myarray.remove(9)
print(myarray)
#8. remove last array element using pop() method
print("Step 8")
myarray.pop(10)
print(myarray)
#9. Fetch any element through its index using index() method
print("Step 9")
print(myarray.index(12))
#10. reverse the array using reverse() method
print("Step 10")
myarray.reverse()
print(myarray)
#11. get array buffer information using buffer_info method
print("Step 11")
print(myarray.buffer_info())
#12. check for number of occurence of an element using count() method
print("Step 12")
myarray.append(12)
print(myarray.count(12))
#13. convert array to string using tostring() method
print("Step 13")
# strTemp = myarray.tostring()
# print(strTemp)
# ints = array('i')
# ints.fromstring(strTemp)
# print(ints)

#14. Convert arrayb to a list using tolist()
print("Step 14")
# print(myarray.tolist())

#15 Slice Elements from an array
print("Step 15")
print(myarray[1:4])