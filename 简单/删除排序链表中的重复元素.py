"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dumpy = ListNode(0)
        dumpy.next = head
        p1, p2 = head, head
        while p2.next:
            if p2.next.val == p1.val:
                p2 = p2.next
                continue
            p2 = p2.next
            p1.next = p2
            p1 = p2
        p1.next = p2.next
        return dumpy.next


if __name__ == '__main__':
    nums = "1,2"
    head = stringToListNode(nums)
    sol = Solution()
    result = sol.deleteDuplicates(head)
    print(listNodeToString(result))
