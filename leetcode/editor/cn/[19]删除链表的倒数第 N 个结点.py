from typing import Optional

from LinkList import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getKthFromEnd(head: ListNode, k: int) -> ListNode:
            '''
            链表中的倒数第N个结点
            :param self:
            :param head:
            :param k:
            :return:
            '''
            p1 = head
            for _ in range(k):
                p1 = p1.next
            while p1:
                p1 = p1.next
                head = head.next
            return head

        dumpy = ListNode(-1)
        dumpy.next = head
        pre_node = getKthFromEnd(dumpy, n + 1)
        pre_node.next = pre_node.next.next
        return dumpy.next

# leetcode submit region end(Prohibit modification and deletion)
