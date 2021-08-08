def countsmaller(nums : list[int])->list[int]:
    count = []
    for i in range(len(nums)):
        c=0
        x = nums[i:len(nums)]
        if len(x)==1:
            count.append(0)
        else:
            x.sort()
            l = 0
            r = len(x)-1
            find = nums[i]
            index=0
            while l<=r:
                mid = l+(r-1)//2
                if x[mid]==find:
                    index = mid
                    break
                elif x[mid]<find:
                    l = mid+1
                else:
                    r = mid-1
            c = index
            count.append(c)
    return count
print(countsmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))