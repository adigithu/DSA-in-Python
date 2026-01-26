class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def deleteAllOccurences(head, key):
    temp = head
    new_head = head
    prev = None
    while temp is not None:
        if temp.data == key:
            if prev is not None:
                prev.next = temp.next
            else:
                new_head = temp.next
            if temp.next is not None:
                temp.next.prev = prev
        else:
            prev = temp
        temp = temp.next
    return new_head
n1 = Node(2)
n2 = Node(2)
n3 = Node(3)
n4 = Node(2)
n5 = Node(10)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4
head = n1
head = deleteAllOccurences(head, 2)
temp = head
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")