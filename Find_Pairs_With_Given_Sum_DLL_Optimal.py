class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def findPairs(head, target):
    result = []
    if head is None:
        return result
    left = head
    right = head
    while right.next is not None:
        right = right.next
    while left is not None and right is not None and left.data < right.data:
        total = left.data + right.data
        if total == target:
            result.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif total > target:
            right = right.prev
        else:
            left = left.next
    return result
n1 = Node(1)
n2 = Node(2)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)
n6 = Node(8)
n7 = Node(9)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4
n5.next = n6
n6.prev = n5
n6.next = n7
n7.prev = n6
head = n1
pairs = findPairs(head, 7)
print(pairs)