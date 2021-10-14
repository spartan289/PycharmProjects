data=[]
n=int(input("enter the no. of elements you want: "))
sum=0
for i in range(0,n):
    x=input("enter the numbers into the array")
    data.append(x)

print(data)
for i in range(0,len(data)):
    sum=sum+int(data[i])
print("sum is ",end=" ")
print(sum)
for i in range(len(data)-1,-1,-1):
    print(int(data[i]))