"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from LinkList import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        ptr = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        ptr.next = l1 if l1 else l2
        return prehead.next


if __name__ == '__main__':
    input1 = "1, 2, 4"
    input2 = "1, 3, 4"
    l1 = stringToListNode(input1)
    l2 = stringToListNode(input2)
    sol = Solution()
    l = sol.mergeTwoLists(l1, l2)
    print(listNodeToString(l))
