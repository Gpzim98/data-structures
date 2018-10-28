class Node(object):
    next_item = None
    previous_item = None

    def __init__(self, value):
        self.value = value


class Stack(object):
    items = []
    top = None

    def peek(self):
        return self.top

    def add(self, node):
        node.previous_item = self.top
        self.top = node
        self.items.append(node)

    def find(self, node):
        for n in self.items:
            if n.value == node.value:
                return n
        else:
            return False

    def remove(self):
        item = self.top
        self.top = self.top.previous_item
        return item

    def print_stack(self):
        for item in self.items:
            print(item.value)


stack = Stack()
for letter in range(ord('A'), ord('Z')):
    node = Node(chr(letter))
    stack.add(node)

# stack.print_stack()

n = Node('Greg')
stack.add(n)

print(stack.peek().value)

print(stack.remove().value)
print(stack.remove().value)
print(stack.remove().value)
print(stack.remove().value)
print(stack.remove().value)
print(stack.remove().value)

stack.print_stack()
