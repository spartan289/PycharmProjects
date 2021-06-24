def p(nums):
        current = 0
        max_sum = 0
        flag=0
        for i in range(len(nums)):
            if nums[i]==0 or i==(len(nums)-1):
                if i==len(nums)-1:
                    if nums[i]==1:
                        current+=1
                max_sum = max(max_sum,current)
                flag=0
                current = 0
            else:
                current+=1
        return max_sum

x = [1,2,1,3,2,5]
