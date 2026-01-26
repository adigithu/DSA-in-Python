class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def reverseDLL(head):
    if head is None or head.next is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        front = curr.next
        curr.next = prev
        curr.prev = front
        prev = curr
        curr = front
    return prev
n1 = Node(5)
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