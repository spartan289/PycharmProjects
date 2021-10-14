def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i=n-1
    j = k =m-1
    while(k>=0):
        if nums2[i]>nums1[j] or j<0:
            nums1[k]=nums2[i]
            i-=1
            if i<0:
                break
        else:
            nums1[k]=nums1[j]
            j-=1
        k-=1
    print(nums1)
merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
