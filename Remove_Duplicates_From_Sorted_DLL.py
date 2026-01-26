class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def removeDuplicates(head):
    if head is None:
        return head
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            nxt = curr.next
            curr.next = nxt.next
            if nxt.next:
                nxt.next.prev = curr
        else:
            curr = curr.next
    return head
n1 = Node(1)
n2 = Node(3)
n3 = Node(6)
n4 = Node(6)
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
head = removeDuplicates(head)
temp = head
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")