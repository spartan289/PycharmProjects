class node:
    # constructor
    def __init__(self, data=None, next=None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

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
        return self.next

    # return true if the node point to another node
    def hasNext(self):
        return self.next != None

    def setPrev(self,prev):
        self.prev = prev
    def getPrev(self,):
        return self.prev
    def hasPrev(self):
        return self.prev!=None

    def __str__(self):
        return "Node[Data=%s]"%(self.data)
class Linkedlist(object):
    def __init__(self,node=None):
        self.length = 0
        self.head = node
    def __iter__(self):
        current = self.head
        count = 0
        while (current!=None):
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
    def insertatBegin(self,data):
        newNode=node(data,None,None)

        if self.head==None:
            self.head=newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def insertingatEnd(self,data):
        newNode=node(data,None,None)
        currentnode = self.head
        while currentnode.next!=None:
            currentnode=currentnode.next
        currentnode.next=newNode
        newNode.prev=currentnode

    def getnode(self,index):
        currentNode = self.head
        if currentNode==None:
            return None
        i=0
        while i < index and currentNode.next!=None:
            currentNode=currentNode.next
            if currentNode==None:
                break
            i+=1
        return currentNode
    def  insertatpos(self,data,index):
        newNode = node(data)
        if self.head==None or index == 0:
            self.insertatBegin(data)
        elif index>0:
            temp = self.getnode(index)
            if temp==None or temp.next == None:
                self.insertingatEnd(data)
            else:
                newNode.prev = temp
                newNode.next = temp.next
                temp.next.prev=newNode
                temp.next=newNode
                self.length+=1
    #deletion
    def deleteatbegin(self):
        self.head = self.head.next
        self.prev = None

    def deleteatend(self):
        current = self.head
        while current.next!=None:
            current = current.next
        current.prev.next=None
    def deleteatpos(self,pos):
        current = self.head
        count=0
        while count < pos:
            current = current.next
            count+=1
        current.prev.next=current.next
        current.next.prev = current
        # current.prev=current.next
        # if current.next:
        #     current.next.prev=current.prev
        #     current.prev=None
        #     current.data=None



l1=Linkedlist()
l1.insertatBegin(3)
l1.insertatBegin(4)
l1.insertatBegin(5)
l1.__iter__()
l1.insertingatEnd(4)
l1.__iter__()
l1.insertatpos(2,2)
l1.__iter__()
l1.deleteatbegin()
l1.__iter__()
l1.deleteatend()
l1.__iter__()
l1.insertatBegin(1)

l1.insertatBegin(5)
l1.__iter__()
l1.deleteatpos(2)
l1.__iter__()