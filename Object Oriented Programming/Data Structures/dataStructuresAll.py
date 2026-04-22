class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

    #Getters
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

    #Setters
    def setData(self,data):
        self.data = data
    def setNext(self,new_next):
        self.next = new_next

class linkedList:
    def __init__(self):
        self.head = None

    #Getters
    def getHead(self):
        return self.head
    def getTail(self):
        current = self.getHead()
        while current.getNext() is not None:
        current = current.getNext()
        return current

    #Setters
    def setHead(self,new_head):
        self.head = new_head

    #Actions
    def printAll(self):
        current = self.getHead()
        while current is not None:
            print(current.getData())
            current = current.getNext()

    def insertAtBegin(self, new_data):
        newNode = Node(new_data)
        if self.getHead() is None:
            self.setHead(newNode)
            return
        else:
            newNode.setNext(self.getHead())
            self.setHead(newNode)
            return

    def insertAtEnd(self, new_data):
        newNode = Node(new_data)
        if self.getHead() is None:
            self.setHead(newNode)
            return
        else:
            current = self.getHead()
            while current.getNext is not None:
                current = current.getNext()
            current.setNext(newNode)

    def insertAtIndex(self, index, new_data):
        newNode = Node(new_data)
        counter = -1
        current = self.getHead()
        while counter < index:
            current = current.getNext()
            counter += 1
        current.setNext(newNode)




