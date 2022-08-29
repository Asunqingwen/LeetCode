from LinkList import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        for _ in range(k):
            p1 = p1.next
        while p1:
            p1 = p1.next
            head = head.next
        return head

# leetcode submit region end(Prohibit modification and deletion)
