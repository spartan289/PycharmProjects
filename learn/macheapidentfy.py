def isHeap(root):
    if root==None:
        return
    queue = [root]
    bool = True
    while len(queue):
        temp=queue.pop(0)
        if temp.left:
            if temp.left:
                if bool | temp.left.data >= temp.data:
                    return False
                queue.append(temp)
        else:
            bool = False
        if temp.right:
            if bool or temp.right.data>=temp.data:
                return False
            queue.append(temp)
        else:
            bool = False
    return True
