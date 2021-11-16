from typing import List

from LinkList import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
