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


class LinkedList:
    def __init__(self):
        self.head = None
    def getHead(self):
        return self.head
    def setHead(self, new_head):
        self.head = new_head

    def getLast(self):
        current_node = self.getHead()
        while current_node.getNext() is not None:
            current_node = current_node.getNext()
        return current_node

    def insert_at_begin(self, new_data):
        new_node = Node(new_data)
        if self.getHead is None:
            self.setHead(new_node)
            return
        else:
            new_node.setNext(self.getHead())
            self.setHead(new_node)

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        last_node = self.getLast()
        last_node.setNext(new_node)
        last_node = self.getLast()
        last_node.setNext(None)
