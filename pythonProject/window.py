
#{
#  Driver Code Starts
#Initial Template for Python 3
class Solution:
    def recreationalSpot(self, arr, n):
        # Your code goes here
        stack = []

        for x in arr:
            if stack:
                if stack[-1] > x:
                    if len(stack) >= 2 and stack[-2] < x:
                        return True
                    stack = []
                    stack.append(x)
                else:
                    if stack[-1] < x and len(stack) > 1:
                        stack.pop()
                        stack.append(x)
                    else:
                        stack.append(x)
            else:
                stack.append(x)

        if len(stack) >= 2 and stack[-2] < x and stack[-1] > x:
            return True
        return False


if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        if ob.recreationalSpot(arr,n):
        	print("True")
        else:
        	print("False")




# } Driver Code Ends