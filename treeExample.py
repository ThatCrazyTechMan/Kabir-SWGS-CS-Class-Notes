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
        return self.

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
                currentNoide = currentNode.getRight()
            else:
                currentNode.setRight(newNode)
        elif currentNode.getLeft() > data:
            if currentNode.getLeft():
                currentNoide = currentNode.getLeft()

            else:
                currentNode.setLeft(newNode)
        else:
            break

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




