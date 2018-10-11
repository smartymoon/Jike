class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.if_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def length(self):
        return len(self.stack)

    def if_empty(self):
        return len(self.stack) is 0
