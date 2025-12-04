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

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def getSize(self):
        return self.size
    def getTop(self):
        return self.top

    def setTop(self, new_top):
        self.top = new_top
    def addSize(self, add_size):
        self.size += add_size
    def subtractSize(self, subtract_size):
        self.size -= 1

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def push(self, data):
        node = Node(data)
        if self.isEmpty():
            self.setTop(node)
            self.addSize(1)
        else:
            top = self.getTop()
            top.setNext(node)
            self.setTop(node)
            self.addSize(1)

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty!')
            return None
        else:
            top = self.getTop().getData()
            next_element = top.getNext()
            next_element.setNext(None)

            return top

        return None




