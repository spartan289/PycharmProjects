# Definition for singly-linked list.

from typing import Optional




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head
        # i=temp.next
        # while(i):
        #     key = i.val
        #     j = head
        #     while(j.next!=i):
        #         j=j.next
        #     while(j and j.val>key):
        #         p=j.next
        #         p.val=j.val
        #         j = getpreviousNode(j,head)
        #     if(j!=None):
        #         j.next.val=key
        #     else:
        #         head.val=key
        #     i=i.next
        # return head
        sortedlist=None
        current = head
        while(current):
            sortedInsert(sortedlist,current)
            current=current.next
        return sortedlist
def sortedInsert(sortedList: Optional[ListNode],newNode):
    current = None
    if(sortedList==None or sortedList.val>=newNode.val):
        newNode.next=sortedList
        sortedList=newNode

    else:
        current=sortedList
        while current.next!=None and current.next.data<newNode.data:
            current=current.next
        newNode.next=current.next
        current.next=newNode
    return sortedList
def getpreviousNode(currentNode,head):
    temp = head
    while(temp):
        if(temp.next==currentNode):
            return temp
        temp=temp.next
    return None
a = ListNode(0)
b= ListNode(4,a)
c=ListNode(3,b)
d=ListNode(5,c)
e=ListNode(-1,d)
insertionSortList(e)
a = ListNode(3)
b= ListNode(1,a)
c=ListNode(2,b)
d=ListNode(4,c)
insertionSortList(d)