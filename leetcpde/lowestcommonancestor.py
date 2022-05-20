class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def findlca(root,n1,n2):
    if root is None:
        return None
    if root.data==n1 or root.data==n2:
        return root
    leftlca = findlca(root.left,n1,n2)
    rightlca = findlca(root.right,n1,n2)
    if leftlca and rightlca:
        return root
    return leftlca if leftlca is not None else  rightlca
