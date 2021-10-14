def bubblesort(li):
    c=0
    for i in range(len(li)):
        for j in range(0,len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]= li[j+1],li[j]
                c+=1
        print('List after ith pass: ',li)
    print('Total comparision are: ',c)
    print('Sorted Array ', li)
def insertionsort(li):
    c=0
    for i in range(len(li)):
        min = i
        for j in range(i+1,len(li)):
            if li[min]>li[j]:
                min = j
                c+=1
        li[i],li[min] = li[min],li[i]
    print('Total Comparision are',c)
    print('Sorted Array ',li)
print("Enter length of element")
n = int(input())
print("Enter elemnet of bubble sort")
bubble = list(map(int,input().split()))
bubblesort(bubble)
print()
print()
print("Enter length of element")
m = int(input())
print("Enter element of insertion sort :")
insertion = list(map(int,input().split()))
insertionsort(insertion)


