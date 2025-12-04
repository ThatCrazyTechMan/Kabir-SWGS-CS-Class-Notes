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

    def addSize(self, add_size):
        self.size += add_size

    def subtractSize(self, subtract_size):
        self.size -= subtract_size

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

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            currentNode = self.getFront()
            while currentNode is not None:
                print(currentNode.getData())
                currentNode = currentNode.getNext()



    def enqueue(self, data):
        node = Node(data)
        if self.isFull():
            print("Queue is Full")
            return None
        elif self.getSize() < self.maxLength:
            if self.getSize() > 0:
                self.getRear().setNext(node)
                self.addSize(1)
                self.setRear(node)
            elif self.getSize() == 0:
                self.setFront(node)
                self.setRear(node)
                self.size += 1
            return None
        else:
            return "List is full!"

    def dequeue(self):
            if self.size>0:
                output = self.getFront().getData()
                self.setFront(self.getFront().getNext())
                self.subtractSize(1)
                if self.getSize() == 0:
                    self.setRear(None)
                return output
            else:
                return "List is empty!"



queue1 = Queue(5)
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.dequeue()

queue1.printQueue()



