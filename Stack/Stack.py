

class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


items = Stack()
print(items.isEmpty())
items.push(1)
items.push(3)


print(items.peek())
