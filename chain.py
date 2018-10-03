class Chain:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def unshift(self, data):
        newNode = Node(data)
        if self.length is 0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    def insert(self, position, data):
        if position < 0 or position > self.length:
            raise Exception('over range')

        if position is 0:
            self.unshift(data)
        elif position is self.length:
            self.append(data)
        else:
            new_node = Node(data)
            replace_node_pre = self.find(position - 1)
            new_node.next = replace_node_pre.next
            replace_node_pre.next = new_node
            self.length += 1

    def append(self, data):
        newNode = Node(data)
        if self.length is 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def delete(self, position):
        if (position < 0) or position > (self.length - 1):
            raise Exception('over range')

        if position is 0:
            self.head = self.head.next
        elif position is (self.length - 1):
            currentNode = self.find(position - 1)
            currentNode.next = None
            self.tail = currentNode
        else:
            findPreNode = self.find(position - 1)
            findPreNode.next = findPreNode.next.next
        self.length -= 1

    def delete_all(self):
        # todo 如何主动回收垃圾？ 是否已经回收？ 研究垃圾回收机制，根引用消失，关联地址是否会被回收
        self.head = self.tail = None
        self.length = 0

    def update(self, position, data):
        if (position < 0) or position > (self.length - 1):
            raise Exception('over range')

        node = self.find(position)
        node.data = data

    def find(self, index):
        if (index < 0) or index > (self.length - 1):
            raise Exception('over range')

        currentNode = self.head
        while index is not 0:
            currentNode = currentNode.next
            index -= 1
        return currentNode

    def __len__(self):
        return self.length

    def print(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=",")
            currentNode = currentNode.next
        print(' length is:', self.length)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

