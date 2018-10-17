"""
队尾指向最后一个数据的下一个位置
"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.box = []
        self.head = self.tail = 0

    def enqueue(self, data):
        if self.tail == self.capacity - 1:
            if self.head == 0:
                return False

            for index, item in self.box[self.head:]:
                self.box[index - self.head] = item

            self.tail = self.tail - self.head
            self.head = 0

        self.box[self.tail] = data
        self.tail += 1
        return True

    def dequeue(self):
        if self.head != self.tail:
            self.head += 1
            return self.box[self.head - 1]
