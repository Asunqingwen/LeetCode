from LinkList import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumpy = ListNode(0)
        dumpy.next = l1
        p = dumpy
        while l1 and l2:
            if l1.val <= l2.val:
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
                p.next = l1
        if l2:
            p.next = l2
        return dumpy.next
