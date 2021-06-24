class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # method for setting data in datafeilds
    def setData(self, data):
        self.data = data

    # method getting the data feild
    def getData(self, data):
        return self.data

    # method for setting the next feild of node
    def setNext(self, next):
        self.next = next

    # method for getting the next feild of node
    def getNext(self):
        self.next = next

    # return true if the node point to another node
    def hasNext(self):
        return self.next != None

class LinkedList(object):
    def __init__(self, node=None):
        self.length = 0
        self.head = node

    def __iter__(self):
        current = self.head
        count = 0
        while (current != None):
            print(current.data, end=" ")
            count += 1
            current = current.next
        print()

    def length(self):
        current = self.head
        count = 0
        while (current != None):
            count += 1
            current = current.next
        return count

    # method for inserting a node at the beginning
    def insertAtBeginning(self, data):

        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtend(self, data):
        newNode = Node()
        newNode.data = data
        current = self.head
        if self.length == 0:
            self.head = newNode
        else:
            while (current.next != None):
                current = current.next
            current.next = newNode
        self.length += 1

    def insertatPosition(self, data, position):
        newNode = Node()
        newNode.data = data
        previousNode = self.head
        c = 0
        while (c != position - 1):
            c += 1
            previousNode = previousNode.next
        newNode.next = previousNode.next
        previousNode.next = newNode
        self.length += 1

    def removeatbegin(self):
        if self.length == 0:
            print("the list is empty")
        self.head = self.head.next
        self.length -= 1

    def removeAtEnd(self):
        if self.length == 0:
            print("the list is empty")
        else:
            currentNode = self.head
            predNode = self.head
            c = 0
            while currentNode.next != None:
                predNode = currentNode
                currentNode = currentNode.next

            predNode.next = None
            self.length -= 1

    def removeatpos(self, pos):
        count = 0
        previousNode = self.head
        currentNode = self.head
        while currentNode.next != None or count < pos:
            count += 1
            if count == pos:
                previousNode.next = currentNode.next
                self.length -= 1
                return
            else:
                previousNode = currentNode
                currentNode = currentNode.next

    def deleteFromLinkedListWithNode(self,node):
        if self.length == 0:
            return ValueError("List is empty")
        else:
            currentNode = self.head
            previousNode = Node
            found = False
            while not found:
                if currentNode == node:
                    found = True
                elif currentNode is None:
                    raise ValueError("Node not in list")
                else:
                    previousNode = currentNode
                    currentNode = currentNode.next
            if previousNode is None:
                self.head = currentNode
            else:
                previousNode = currentNode.next
            self.length -= 1

    def clear(self):
        self.head = None

    def reverselist(self):
        prev = None
        current = self.head
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev
        return prev




l1 = LinkedList()
l2 = LinkedList()
li=[2,3,4,5]
l1.insertAtBeginning(1)
for i in li:
    l1.insertAtend(i)
l1.__iter__()
# l2.__iter__()
# l3 = LinkedList()
# i = 0
# carry = 0
# x = l1.length
# y = l2.length
# current1 = l1.head
# current2 = l2.head
# if x>=y:
#     while i < x:
#         if i < y:
#             if current1.data+current2.data+carry <10:
#                 l3.insertAtend(current1.data+current2.data+carry)
#                 carry = 0
#             if current1.data+current2.data+carry>=10:
#                 l3.insertAtend(current2.data+carry+current1.data-10)
#                 carry = 1
#         if i>=y:
#             if carry == 1:
#                 if current1.data+carry==10:
#                     l3.insertAtend(0)
#                 else:
#                     l3.insertAtend(current1.data+carry)
#                     carry = 0
#             else:
#                 l3.insertAtend(current1.data)
#         i+=1
#         if current1: current1 = current1.next
#         if current2: current2 = current2.next
# elif y>x:
#     while i < y:
#         if i < x:
#             if current1.data+current2.data+carry <10:
#                 l3.insertAtend(current1.data+current2.data+carry)
#                 carry = 0
#             if current1.data+current2.data+carry>=10:
#                 l3.insertAtend(current2.data+carry+current1.data-10)
#                 carry = 1
#         if i>=x:
#             if carry == 1:
#                 if current2.data+carry==10:
#                     l3.insertAtend(0)
#                 else:
#                     l3.insertAtend(current2.data+carry)
#                     carry = 0
#             else:
#                 l3.insertAtend(current2.data)
#         i+=1
#         if current1: current1 = current1.next
#         if current2: current2 = current2.next
#
# if carry == 1:
#     l3.insertAtend(1)
# l3.__iter__()
#
# l3.removeatpos(1)
# l3.__iter__()
x = LinkedList()
x.__iter__()
if x==l1:
    print(True)
else:
    print(False)


