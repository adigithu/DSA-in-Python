class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def oddEvenList(head):
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next        
    even_head = even           
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head
n1 = ListNode(8)
n2 = ListNode(1)
n3 = ListNode(6)
n4 = ListNode(9)
n5 = ListNode(7)
n6 = ListNode(5)
n7 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
head = n1
head = oddEvenList(head)
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")