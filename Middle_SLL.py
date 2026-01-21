class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def middleNode(self, head: Node) -> Node:
        slow = head
        fast = head

        # Move slow by 1 step and fast by 2 steps
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
node1 = Node(6)
node2 = Node(8)
node3 = Node(9)
node4 = Node(11)
node5 = Node(22)
node6 = Node(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
obj = Solution()
middle = obj.middleNode(node1)
print("Middle node value:", middle.val)