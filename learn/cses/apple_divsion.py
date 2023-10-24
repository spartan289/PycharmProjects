n = int(input())
arr = list(map(int,input().split()))
total_sum = sum(arr)
def minimumdiff(arr,current_sum,total_sum,i):
    if i==0:
        return abs(total_sum-2*current_sum)
    else:
        return min(minimumdiff(arr,current_sum+arr[i],total_sum,i-1),minimumdiff(arr, current_sum, total_sum, i-1))

print(minimumdiff(arr,0,total_sum,n-1))

