class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def reverseDLL(head):
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next
    return head
n1 = Node(9)
n2 = Node(3)
n3 = Node(2)
n4 = Node(1)
n5 = Node(9)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4
head = n1
head = reverseDLL(head)
temp = head
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")