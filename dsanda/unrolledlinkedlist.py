#Node of a singly linked list
class Node:
    def __init__(self):
        self.value = None
        self.next = None
class LinkedBlock:
    def __init__(self):
        self.head=None
        self.next = None
        self.nodeCount = 0

blocksize=0
blockHead=None

def newlinkedblock():
    block = LinkedBlock()
    block.next = None
    block.head = None
    block.nodeCount = 0
    return block


def newNode(value):
    temp = Node()
    temp.next = None
    temp.value = None
    return temp
def searchElements(blockHead, k):
    #find the block
    j = (k+blocksize-1)//blocksize #kth node is in jth block
    p = blockHead
    j-=1
    while(j):
        p=p.next
        j-=1
    flinkedblock = p

    #find the node
    q=p.head
    k=k%blocksize
    if k==0:
        k=blocksize
    k=p.nodeCount+1-k
    k-=1
    while(k):
        q=q.next
        k-=1
    fnode=q
    return  flinkedblock,fnode
