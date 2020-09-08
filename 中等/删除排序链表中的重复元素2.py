"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
"""
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dumpy = ListNode(0)
        dumpy.next = head
        p1, p2, p3 = dumpy, head, head
        count = 0
        while p3.next:
            if p3.next.val == p2.val:
                p3 = p3.next
                count += 1
                continue
            p3 = p3.next
            p2 = p3
            if count > 0:
                p1.next = p3
            else:
                p1 = p1.next
            count = 0
        if count > 0:
            p1.next = p3.next
        return dumpy.next


if __name__ == '__main__':
    nums = "1,1,1,1"
    head = stringToListNode(nums)
    sol = Solution()
    result = sol.deleteDuplicates(head)
    print(listNodeToString(result))
