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
                    previousNode=currentNode
                    currentNode=currentNode.next
            if previousNode is None:
                self.head = currentNode
            else:
                previousNode = currentNode.next
            self.length -= 1
    def clear(self):
        self.head = None

l1 = LinkedList()
l1.insertAtBeginning(4)
l1.insertAtBeginning(5)
l1.insertAtend(6)
l1.insertAtend(3)
l1.insertatPosition(2, 2)
l1.__iter__()
print(l1.length)
l1.insertatPosition(7, 3)
l1.__iter__()
l1.removeatbegin()
l1.__iter__()
l1.__iter__()
l1.removeAtEnd()
l1.removeAtEnd()
l1.__iter__()
l1.__iter__()
l1.removeatpos(2)
l1.__iter__()
l1.clear()
l1.__iter__()
print(1)
l1.__iter__()