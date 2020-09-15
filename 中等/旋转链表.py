"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        p1 = head
        lenh = 0
        while p1.next:
            p1 = p1.next
            lenh += 1
        lenh += 1
        k %= lenh
        if k == 0:
            return head

        dumpy = ListNode(0)
        dumpy.next = head
        p2 = head
        for _ in range(lenh - k - 1):
            p2 = p2.next
        dumpy.next = p2.next
        p1.next = head
        p2.next = None

        return dumpy.next


if __name__ == '__main__':
    nums = "1,2,3,4,5"
    k = 2
    head = stringToListNode(nums)
    sol = Solution()
    print(listNodeToString(sol.rotateRight(head, k)))
