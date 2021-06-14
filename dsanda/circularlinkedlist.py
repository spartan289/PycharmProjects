# class Node:
#     # constructor
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     # method for setting data in datafeilds
#     def setData(self, data):
#         self.data = data
#
#     # method getting the data feild
#     def getData(self, data):
#         return self.data
#
#     # method for setting the next feild of node
#     def setNext(self, next):
#         self.next = next
#
#     # method for getting the next feild of node
#     def getNext(self):
#         return self.next
#
#     # return true if the node point to another node
#     def hasNext(self):
#         return self.next != None
#
# class LinkNode():
#     def __init__(self, node=None):
#         self.head = node
#         if node:
#             node.next = self.head  # Establish a loop head node
#
#     def is_empty(self):
#         """Judging whether the list is empty"""
#         return self.head == None
#     def circularList(self):
#         currentnode=self.head
#         if currentnode == None:
#             return 0
#         count = 1
#         currentnode = currentnode.next
#         while currentnode !=self.head:
#             currentnode=currentnode.next
#             count+=1
#         return count
#
#     def printcircularlist(self):
#         currentnode=self.head
#         if currentnode == None:
#             return 0
#         print(currentnode.data)
#         while currentnode != self.head:
#             currentnode = currentnode.next
#             print(currentnode.data)
#
#     def insertatEnd(self,data):
#         current = self.head
#         newNode = Node(data)
#         if self.head == None:
#             self.head = newNode
#         else:
#             while current.next != self.head:
#                 current=current.next
#             current.next = newNode
#             newNode.next = self.head
#
#     def TailInsert(self, num):
#         """
#             //Tail insertion node
#         # """
#         node = Node(num)
#         if self.is_empty():
#             self.head = node
#             node.next = self.head
#         else:
#             cur = self.head
#             while cur.next != self.head:
#                 cur = cur.next
#             cur.next = node
#             node.next = self.head


import random


class Node():
    """
        //Establishing Nodes
    """

    def __init__(self, date):
        self.date = date
        self.next = None


class LinkNode():
    def __init__(self, node=None):
        self.head = node
        if node:
            node.next = self.head  # Establish a loop head node

    def is_empty(self):
        """Judging whether the list is empty"""
        return self.head == None

    def length(self):
        """
            //Finding the Length of Chain List
        """
        if self.is_empty():
            return 0

        count = 1
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """Traversing the entire list"""
        if self.is_empty():
            return
        # Creating a cursor equals the starting node
        cur = self.head
        while cur.next != self.head:
            print(cur.date, end=" ")
            cur = cur.next
        print(cur.date, end="\n")

    def HeadInsert(self, num):
        """
            //Head insertion node
        """
        node = Node(num)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            self.head = node
            cur.next = self.head

    def TailInsert(self, num):
        """
            //Tail insertion node
        """
        node = Node(num)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def NodeInsert(self, index, num):
        """Adding elements at specified locations"""
        # Point to the address of self. head, which is not a header element
        # For the next element, so Preis the next element
        if index <= 0:
            # Think of it as head insertion.
            self.HeadInsert(num)
        elif index > (self.length() - 1):
            self.TailInsert(num)
        else:
            pre_cur = self.head
            count = 0
            while count < (index - 1):
                count += 1
                pre_cur = pre_cur.next
            node = Node(num)
            node.next = pre_cur.next
            pre_cur.next = node
l1 = LinkNode()
l1.TailInsert(3)

l1.TailInsert(4)
l1.TailInsert(5)
l1.TailInsert(6)
l1.travel()