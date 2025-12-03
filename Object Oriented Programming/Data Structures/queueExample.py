class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data
    def setNext(self, new_next):
        self.next = new_next


class Queue:
    def __init__(self, maxLength):
        self.front = None
        self.rear = None
        self.maxLength = maxLength
        self.size = 0

    def getFront(self):
        return self.front

    def getRear(self):
        return self.rear

    def getSize(self):
        return self.size

    def setRear(self, new_rear):
        self.rear = new_rear

    def setFront(self, new_front):
        self.front = new_front

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.getSize() == self.maxLength:
            return True
        else:
            return False



    def enqueue(self, data):
        node = Node(data)
        if self.size < self.maxLength:
            if self.size>0:
                self.getRear().setNext(node)
                self.size += 1
                self.setRear(node)
            elif self.getSize() == 0:
                self.setFront(node)
                self.setRear(node)
                self.size += 1
            return None
        else:
            return "List is full!"

    def dequeue(self):
        if self.getSize() < self.maxLength:
            if self.size>0:
                output = self.getFront()



