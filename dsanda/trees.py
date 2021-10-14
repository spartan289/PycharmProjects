import collections


class BinaryTreeNode :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self,root=None):
        self.root = root
    def preorder(self,root):
        if root==None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def levelorder(self,root):
        if root is None:
            return
        hd_node = {}
        q = [root]
        hash = {}
        hash[0]=[root.data]
        hd_node[root]=0
        while len(q)!=0:
            temp = q.pop(0)
            if temp.left:
                q.append(temp.left)
                hd_node[temp.left] = hd_node[temp]-1
                hd = hd_node[temp.left]

                if hash.get(hd) is None:
                    hash[hd]=[]
                hash[hd].append(temp.left.data)
            if temp.right:
                q.append(temp.right)
                hd_node[temp.right] = hd_node[temp] - 1
                hd = hd_node[temp.right]

                if hash.get(hd) is None:
                    hash[hd] = []
                hash[hd].append(temp.right.data)
        sorted_hash = collections.OrderedDict(sorted(hash.items()))
        result = []
        for i in sorted_hash:
            result += sorted_hash[i]
        return result
    def checkbst(self,root):
        if root==None:
            return
        stack = []
        stack.append([root,float('-inf'),float('inf')])

        while(len(stack)!=0):
            temp = stack.pop()
            if temp[0].data>temp[1] and temp[0].data<temp[2]:
                pass
            else:
                return 0
            if temp[0].left:
                stack.append([temp[0].left,temp[1],temp[0].data])
            if temp[0].right:
                stack.append([temp[0].right,temp[0].data,temp[2]])
        return 1




bin1 = BinaryTreeNode(8)
bin2 = BinaryTreeNode(2)
bin3 = BinaryTreeNode(3)
bin4 = BinaryTreeNode(4)
bin5 = BinaryTreeNode(5)
bin6 = BinaryTreeNode(6)
bin7 = BinaryTreeNode(7)

bin1.right = bin3
bin1.left = bin2
bin2.left = bin4
bin2.right = bin5
bin3.left = bin6
bin3.right = bin7
binary = BinaryTree(bin1)
binary.preorder(bin1)
print(binary.levelorder(bin1))
