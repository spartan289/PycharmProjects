def checktree(preorder,inorder,postorder,n):
    x = sorted(preorder)
    y = sorted(inorder)
    z = sorted(postorder)
    if x!=y or x!=z or y!=z:
        return False
    def chftree(preorder,inorder,postorder,n):
        if n==0:
            return 1
        if n==1:
            return preorder[0]==inorder[0] and inorder[0]==postorder[0]
        index = -1
        for i in range(n):
            if inorder[i]==preorder[0]:
                index=i
                break
        if index==-1:
            return 0
        ret1 = chftree(preorder[1:],inorder,postorder, index)
        ret2 = chftree(preorder[index+1:],inorder[index+1:],postorder[index:],n-index-1)
        return ret1 and ret2
    if chftree(preorder,inorder,postorder,n):
        return True
    else:
        return False
print(checktree([1,2,4,5,3],[4, 2, 5,1, 3],[4,5,2,3,10],5))

