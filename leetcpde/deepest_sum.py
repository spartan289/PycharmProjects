# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
class Solution:
    def dfs(self, node):
        if node==None:
            return 0
        return 1+ max(self.dfs(node.left),self.dfs(node.right))
    def deepestLeavesSum(self, root: Optional[TreeNode]):
        depth = self.dfs(root)
        sum = self.max_sum(root,depth)
        return sum
    def max_sum(self,node,depth):
        if node==None:
            return 0
        if depth==1:
            if(node.val):
                return node.val
        return  self.max_sum(node.left,depth-1)+self.max_sum(node.right,depth-1)

arr = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
def converttoTree(arr,root,i,n):
    if i<n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = converttoTree(arr,root.left,2*i+1,n)
        root.right = converttoTree(arr,root.right,2*i+2,n)
    return root

root = converttoTree(arr,None,0,len(arr))

s = Solution()
s.deepestLeavesSum(root)

