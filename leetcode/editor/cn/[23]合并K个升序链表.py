'''
堆排序的应用
'''
from typing import Optional, List

from LinkList import ListNode

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dumpy = p = ListNode(-1)
        pq = []
        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(pq, (lists[idx].val, idx))

        while pq:
            val, idx = heapq.heappop(pq)
            p.next = ListNode(val)
            p = p.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(pq, (lists[idx].val, idx))

        return dumpy.next
# leetcode submit region end(Prohibit modification and deletion)
