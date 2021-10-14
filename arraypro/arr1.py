#importing array as array creations
import array as arr

#array with int type
a=arr.array('i',[1,2,3])
print("array before insertion : ",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print()
a.insert(1,4)
print("array after insertion : ",end=" ")
for i in (a):
    print(i,end=" ")
print()
#array with float type
b=arr.array('d',[2.5,3.2,3.3])
print("array before insertion : ",end=" ")
for i in range(0,3):
    print(b[i],end=" ")

print()
print("array after append : ",end=" ")
b.append(4.4)
for i in (b):
    print(i,end=" ")