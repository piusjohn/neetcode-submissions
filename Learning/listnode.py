class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(12)
node2 = Node(13)
node3 = Node(14)
node4 = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

current = head

while current:
    print(current.data, end=" -> ")
    current = current.next
print(None)