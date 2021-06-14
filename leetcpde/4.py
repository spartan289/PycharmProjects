def median(li):
    if len(li)==0:
        return "{:.5f}".format(0)
    elif len(li)==1:
        return "{:.5f}".format(li[0])
    if (len(li))%2!=0:
        return "{:.5f}".format(li[(len(li)-1)//2])
    else:
        return "{:.5f}".format((li[(len(li))//2-1]+li[(len(li))//2])/2)


def findMedianSortedArrays(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    li=[]
    i=0
    j=0
    while (j+i)!=(n+m) and i!=m and j!=n:
        if nums1[j]<nums2[i]:
            li.append(nums1[j])
            j+=1
        else:
            li.append(nums2[i])
            i+=1
    if j+i!=n+m:
        if i==m:
            while j<n:
                li.append(nums1[j])
                j+=1
        if j==n:
            while i<m:
                li.append(nums2[i])
                i+=1
    return median(li)
def findMedian(nums1,nums2):
    nums = nums1+nums2
    nums.sort()
    n = len(nums)
    m = int(len(nums) / 2)

    if n % 2 == 0:
        middle1 = nums[m - 1]
        middle2 = nums[m]
        median = (middle1 + middle2) / 2
    else:
        median = nums[m]

    return median

findMedianSortedArrays([1,2],[3,4,5])