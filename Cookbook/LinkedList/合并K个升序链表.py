'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
'''
from typing import List

from LinkList import stringToListNode, ListNode, listNodeToString


class Solution:
    def merge(self, l1: ListNode, l2: ListNode):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        l2.next = self.merge(l1, l2.next)
        return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        len_ = len(lists)
        if len_ < 1:
            return None
        if len_ == 1:
            return lists[0]

        mid = len_ // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)


if __name__ == '__main__':
    lists = [stringToListNode("1,4,5"), stringToListNode("1,3,4"), stringToListNode("2,6")]
    sol = Solution()
    print(listNodeToString(sol.mergeKLists(lists)))
