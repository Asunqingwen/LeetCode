'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
'''
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dumpy = ListNode(0)
        dumpy.next = head
        p = dumpy
        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            p = p.next
        p.next = p.next.next
        return dumpy.next


if __name__ == '__main__':
    nums = "1"
    n = 1
    head = stringToListNode(nums)
    sol = Solution()
    print(listNodeToString(sol.removeNthFromEnd(head, n)))
