"""
队尾指向最后一个数据的下一个位置
"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.box = []
        self.head = self.tail = 0

    def enqueue(self, data):
        if self.tail == self.capacity:
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

    def __repr__(self):
        print(",".join(map(str, self.box[self.head:self.tail])))


class CirQueue:
    def __init__(self, capacity):
        self.box = []
        self.capacity = capacity + 1  # +1 多了一个空白位，用于判断满队
        self.head = self.tail = 0

    def enqueue(self, data):
        # 队满后不允许入队
        if (self.tail + 1) % self.capacity == self.head:
            return False
        else:
            self.box[self.tail] = data
            self.tail = (self.tail + 1) % self.capacity
            return True

    def dequeue(self):
        if self.tail == self.head:
            return None
        else:
            data = self.box[self.head]
            self.head = (self.head + 1) % self.capacity
            return data

    def __repr__(self):
        if self.tail > self.head:
            print(",".join(map(str, self.box[self.head:self.tail])))
        else:
            print(",".join(map(str, self.box[self.head:] + self.box[:self.tail])))
