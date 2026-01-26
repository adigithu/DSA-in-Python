class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
    length = 0
    temp = head
    while temp is not None:
        length += 1
        temp = temp.next
    if length == n:
        return head.next
    position_to_stop = length - n
    temp = head
    count = 1
    while count < position_to_stop:
        temp = temp.next
        count += 1
    temp.next = temp.next.next
    return head
n1 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(7)
n5 = ListNode(1)
n6 = ListNode(2)
n7 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
head = n1
head = removeNthFromEnd(head, 2)
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")