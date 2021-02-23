'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
'''
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumpy = ListNode(0)
        add1, add2, ans, p = 0, 0, 0, dumpy
        while l1 or l2:
            if l1:
                add1 = l1.val
                l1 = l1.next
            if l2:
                add2 = l2.val
                l2 = l2.next
            ans, mod = divmod(add1 + add2 + ans, 10)
            add1 = add2 = 0
            p.next = ListNode(mod)
            p = p.next
        if ans > 0:
            p.next = ListNode(ans)
        return dumpy.next


if __name__ == '__main__':
    nums1 = "9,9,9,9,9,9,9"
    nums2 = "9,9,9,9"
    l1 = stringToListNode(nums1)
    l2 = stringToListNode(nums2)
    sol = Solution()
    print(listNodeToString(sol.addTwoNumbers(l1, l2)))
