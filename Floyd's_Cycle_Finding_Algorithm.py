class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def length_of_loop(head):
    if not head or not head.next:
        return 0
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0
n1 = ListNode(5)
n2 = ListNode(9)
n3 = ListNode(1)
n4 = ListNode(7)
n5 = ListNode(6)
n6 = ListNode(1)
n7 = ListNode(9)
n8 = ListNode(2)
n9 = ListNode(8)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n3
head = n1
print("Length of loop:", length_of_loop(head))