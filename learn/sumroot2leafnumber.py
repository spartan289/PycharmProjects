from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def preorder(self,root,total_sum,ans):

        total_sum = total_sum*10+root.val
        if root.left ==None and root.right==None:
            ans[0]+=total_sum
            total_sum = total_sum//10
        if root.left: preorder(root.left,total_sum,ans)
        if root.right: preorder(root.right,total_sum,ans)

def sumNumbers(self, root: Optional[TreeNode]) -> int:
    ans = [0]
    preorder(root, 0, ans)
    return ans[0]


root = TreeNode(4)
root.left=TreeNode(9)
root.right = TreeNode(0)
root.left.left=TreeNode(5)
root.left.right=TreeNode(1)
ans=[]
