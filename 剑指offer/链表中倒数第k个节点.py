from LinkList import ListNode

class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        len_ = 0
        while p:
            len_ += 1
            p = p.next
        if len_ < k:
            return None
        p = head
        for _ in range(k):
            p = p.next
        for _ in range(len_-k):
            p = p.next
            head = head.next
        return head