class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_value = None


class Queue(object):
    def __init__(self):
        self.items = []
        self.last = None

    def push(self, node):
        node.next_value = self.last
        self.last = node
        self.items.append(node)

    def remove(self):
        item = self.items[0]
        self.items.remove(item)
        return item

    def print_queue(self):
        for item in self.items:
            print(item.value)


node = Node('Greg')
q = Queue()
q.push(node)
q.print_queue()
print('Removed' + str(q.remove().value))
q.print_queue()