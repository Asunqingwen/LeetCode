from LinkList import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dumpy = ListNode(0)
        dumpy.next = head
        p = dumpy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                return dumpy.next
            p = p.next
        return dumpy.next
