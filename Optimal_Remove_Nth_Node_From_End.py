class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
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