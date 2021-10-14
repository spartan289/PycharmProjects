def reverse(a,start,end):
    while start<end:
        a[start],a[end]=a[end],a[start]
        start+=1
        end-=1

a=[]
n=int(input("enter number of element in array"))
for i in range(0,n):
    x=int(input("enter elements of the array"))
    a.append(x)
print(a)
print("reverse array is: ")
reverse(a,0,len(a)-1)
print(a)