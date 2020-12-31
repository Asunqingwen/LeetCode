'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumpy = ListNode(0)
        dumpy.next = l1
        l = dumpy
        ans = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            ans += a + b
            ans, mod = divmod(ans, 10)
            l.next = ListNode(mod)
            l = l.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if ans > 0:
            l.next = ListNode(1)
        return dumpy.next


if __name__ == '__main__':
    nums1 = "9"
    nums2 = "9"
    l1 = stringToListNode(nums1)
    l2 = stringToListNode(nums2)
    sol = Solution()
    print(listNodeToString(sol.addTwoNumbers(l1, l2)))
