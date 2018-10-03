class Link:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def unshift(self, data):
        if self.length is 0:
            self.head = self.tail = Node(data)
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insert(self, index, data):
        if index < 0 or (index > self.length):
            raise Exception('over range')

        if index is 0:
            self.unshift(data)
        elif index is self.length:
            self.append(data)
        else:
            newNode = Node(data)
            replaceNode = self.find(index)

            replaceNode.prev.next = newNode
            newNode.prev = replaceNode.prev

            newNode.next = replaceNode
            replaceNode.prev = newNode

            self.length += 1

    def append(self, data):
        if self.length is 0:
            self.head = self.tail = Node(data)
        else:
            newNode = Node(data)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

    def delete(self, index):
        currentNode = self.find(index)
        if index is 0:
            currentNode.next.prev = None
            self.head = currentNode.next
        elif index is (self.length - 1):
            currentNode.prev.next = None
            self.tail = currentNode.prev
        else:
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev

        self.length -= 1

    def delete_all(self):
        self.head = self.tail = None
        self.length = 0

    def find(self, index):
        self.check(index)
        currentNode = self.head
        while index != 0:
            currentNode = currentNode.next
            index -= 1
        return currentNode

    def check(self, index):
        if index < 0 or (index > (self.length - 1)):
            raise Exception('over range')

    def update(self, index, data):
        currentNode = self.find(index)
        currentNode.data = data

    def __len__(self):
        return self.length

    def print(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=',')
            currentNode = currentNode.next
        print('length is:', self.length)


class Node:
    def __init__(self, data):
        self.next = self.prev = None
        self.data = data

