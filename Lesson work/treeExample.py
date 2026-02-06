class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


    def setLeft(self, newLeft):
        self.left = newLeft

    def setRight(self, newRight):
        self.right = newRight


class binaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root()

    def getRootData(self):
        return self.getRoot().getData()

    def setRoot(self, newRoot):
        self.root = newRoot

    def insertNode(self, data):
        newNode = Node(data)
        if not self.getRoot():
            self.setRoot(newNode)
            return

        currentNode= self.getRoot()
        if currentNode.getData() < data:
            if currentNode.getRight():
                currentNode = currentNode.getRight()
            else:
                currentNode.setRight(newNode)
        elif currentNode.getLeft() > data:
            if currentNode.getLeft():
                currentNode = currentNode.getLeft()

            else:
                currentNode.setLeft(newNode)
        else:
            return

    def inOrder(self, node):
        if node:
            self.inOrder(node.getLeft())
            print(node.getData(), end='')
            self.inOrder(node.getRight())


    def preOrder(self, node):
        if node:
            print(node.getData(), end='')
            self.preOrder(node.getLeft())
            self.preOrder(node.getRight())

    def postOrder(self, node):
        if node:
            self.postOrder(node.getLeft())
            self.postOrder(node.getRight())
            print(node.getData(), end='')

    def binarySearch(self, term):
        current_node = self.getRoot()
        while current_node.getData() != term:
            if current_node.getRight() == None and current_node.getLeft() == None:
                return "Node not found"
                break
            if term > current_node.getData():
                current_node = current_node.getRight()
            else:
                current_node = current_node.getLeft()
            if current_node.getData() == term:
                return f"Data found at {current_node}"
                break







