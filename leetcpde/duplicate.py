def duplicate(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow==fast:
            break
    slow = nums[0]
    while slow!=fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
print(duplicate([1,2,3,4,5,6,7,3,8]))