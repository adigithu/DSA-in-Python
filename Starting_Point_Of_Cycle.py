class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

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

sol = Solution()
cycle_node = sol.detectCycle(head)

if cycle_node:
    print("Cycle starts at node with value:", cycle_node.val)
else:
    print("No cycle detected")