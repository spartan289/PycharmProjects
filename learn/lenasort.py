def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l
def lena_sort(nums):
    c=0
    if len(nums)<=1 :
        return nums,c
    pivot = nums[0]
    less = []
    more = []
    for i in range(1,len(nums)):
        if nums[i]<pivot:
            less.append(nums[i])
        else:
            more.append(nums[i])
        c+=1
    x=0
    sorted_less,x = lena_sort(less)
    c+=x
    sorted_more,x = lena_sort(more)
    c+=x
    sorted_less.append(pivot)
    ans = sorted_less+sorted_more
    
    return ans,c

data=[1,2,3,4,5]
for p in permutation(data):
    print(p,end=" ")
    print(lena_sort(p))
    
    