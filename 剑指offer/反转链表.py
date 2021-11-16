from LinkList import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dumpy = ListNode(0)
        while head:
            tmp = head
            head = head.next
            tmp.next = dumpy.next
            dumpy.next = tmp
        return dumpy.next
