class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield  node
            node = node.next
    def insertSLL(self, value, location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location == 1:
                newNode.next =None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index=0
                while index<location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    #traverse single linked list
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node=node.next
    def searchinSLL(self,nodevalue):
        if self.head is None:
            return "The list does not exist"
        else:
            node=self.head
            while node is not None:
                if node.value==nodevalue:
                    return node.value
                node=node.next
            return "The value does not exist in list"
    def deleteNode(self,location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head = self.head.next
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode = self.head
                index=0
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deletentirelinkedlist(self):
        if self.head is None:
            print("The single linnked list is none")
        else:
            self.head = None
            self.tail = None
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
singlylinkedlist = SLinkedList()
node1 = Node(1)
node2 = Node(2)
singlylinkedlist.insertSLL(1,1)
singlylinkedlist.insertSLL(2,1)
singlylinkedlist.insertSLL(3,1)
singlylinkedlist.insertSLL(4,1)
singlylinkedlist.insertSLL(5,1)
singlylinkedlist.insertSLL(0,0)
singlylinkedlist.insertSLL(0,3)
print([node.value for node in singlylinkedlist])
print(singlylinkedlist.searchinSLL(3))
singlylinkedlist.deleteNode(0)
singlylinkedlist.deleteNode(1)
singlylinkedlist.deleteNode(3)

print([node.value for node in singlylinkedlist])
singlylinkedlist.deletentirelinkedlist()
print([node.value for node in singlylinkedlist])
