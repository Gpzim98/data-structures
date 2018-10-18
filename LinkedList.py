# Add - ok
# Remove - ok
# Find - ok
# Get root - ok
# Get top - ok
# Remove root - ok
# Remove top
# Print List


class Node(object):
    value = None
    next = None

    def __init__(self, value=None):
        self.value = value

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return self.value


class LinkedList(object):
    root = Node()
    top = Node()

    def __init__(self, node=None):
        self.root = node

    def get_last_element(self):
        next = self.root.get_next()

        while next:
            if not next.get_next():
                return next
            else:
                next = next.get_next()

    def add(self, node):
        if self.root.get_next():
            last_element = self.get_last_element()
            last_element.next = node
            self.top = node
        else:
            self.root.set_next(node)

    def find_node_by_value(self, value):
        node = self.root

        while node.next:
            if node.value == value:
                return node
            else:
                node = node.next

    def get_previous_node(self, node_find):
        if node_find == self.root:
            return False

        node = self.root

        while node:
            if node.next == node_find:
                return node
            else:
                node = node.next

    def remove(self, node):
        previous_node = self.get_previous_node(node)

        if previous_node:
            previous_node.next = node.next
            return True

    def get_root(self):
        return self.root

    def get_top(self):
        return self.top

    def remove_root(self):
        self.root = self.root.next

    def remove_top(self):
        previous_node = self.get_previous_node(self.top)
        self.top = previous_node

    def print_list(self):
        node = self.root

        while node.next:
            print(node)
            node = node.next

        print(node)


root = Node('Root')
linked_list = LinkedList(root)

node = Node('A')

for i in range(0, 10):
    node = Node('Node ' + str(i))
    linked_list.add(node)

linked_list.remove(node)
node17 = linked_list.find_node_by_value('Node 17')
linked_list.remove(node17)
linked_list.print_list()

print(linked_list.get_root())
print('top')
print(linked_list.get_top())

linked_list.remove_root()
print('New root')
print(linked_list.get_root())

print('top')
print(linked_list.get_top())
linked_list.remove_top()
print('New top')
print(linked_list.get_top())