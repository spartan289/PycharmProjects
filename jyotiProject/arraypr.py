#arrays types can hold homogeneous datatypes and operate
#on them efficiently while using less memory

from array import array

#create an array of integer numbers
arr1=array('i',[2,4,6,8,10,12,14,16,18])
print(arr1.typecode)
print("array1 item size", arr1.itemsize)

#Add additional item to the array
arr1.insert(0,0)
arr1.append(22)
arr1.extend([24,34,56])
print(arr1)
#iterate over the array content like any other list
for i,elem in enumerate(arr1):
    arr1[i] = elem*2
print(arr1)
#try to add a non-integer number to the array


#create an array to hold a bytes instead of ints
arr2=array('B',[18,102,182,56,89,5,254,32,64,50])
print(arr2.typecode)
print(arr2.itemsize)
#try to add an item that's out of range
#arr2.append(300)

#convert an array to a list
list1=arr2.tolist()
print(list1)