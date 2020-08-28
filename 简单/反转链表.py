"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = ListNode(0)
        p = head
        while head:
            head = head.next
            p.next = res.next
            res.next = p
            p = head
        return res.next



if __name__ == '__main__':
    nums = "1,2,3,4,5"
    head = stringToListNode(nums)
    sol = Solution()
    result = sol.reverseList(head)
    print(listNodeToString(result))
