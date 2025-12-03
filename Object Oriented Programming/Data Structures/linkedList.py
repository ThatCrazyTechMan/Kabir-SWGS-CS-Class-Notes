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

    def printAll(self):
        current_node = self.getHead()
        while current_node.getNext() is not None:
            print(current_node.getData())
            current_node = current_node.getNext()

    def insert_at_begin(self, new_data):
        new_node = Node(new_data)
        if self.getHead is None:
            self.setHead(new_node)
            return
        else:
            new_node.setNext(self.getHead())
            self.setHead(new_node)

    def insert_at_end(self, new_data):
        if self.getHead() is None:
            node = Node(new_data)
            self.setHead(node)
        else:
            new_node = Node(new_data)
            last_node = self.getLast()
            last_node.setNext(new_node)

    def insert_at_index(self, new_data, index):
        counter = 0
        current_node = self.getHead()
        if index == 0:
            node = Node(new_data)
            self.setHead(node)
        while counter != index -1:
            current_node = current_node.getNext()
            counter += 1
        current_node.setNext(new_data)


    def delete_at_begin(self):
        current_node = self.getHead()
        next_node = current_node.getNext()
        if current_node is None:
            return
        else:
            self.setHead(next_node)
            current_node = None

    def delete_at_end(self):
        current_node = self.getLast()
        current_node.setData(None)



list = LinkedList()
list.insert_at_begin('France')
list.insert_at_begin('Germany')
list.insert_at_begin('Spain')
list.insert_at_begin('Belgium')
list.insert_at_end('Brazil')
list.delete_at_begin()
list.insert_at_index('Norway', 2)
list.printAll()