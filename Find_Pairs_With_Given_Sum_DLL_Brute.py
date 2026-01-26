class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def findPairs(head, target):
    temp1 = head
    result = []
    while temp1 is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.data + temp2.data == target:
                result.append((temp1.data, temp2.data))
            temp2 = temp2.next
        temp1 = temp1.next
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