"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
from LinkList import ListNode, stringToListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lenh = 0
        p = head

        # 链表长度
        while p:
            lenh += 1
            p = p.next

        # 后半部分
        mid = (lenh + 1) // 2
        left, rightp = head, head
        for _ in range(mid):
            rightp = rightp.next

        # 后半部分翻转
        dumpy = ListNode(0)
        while rightp:
            tmp = rightp.next
            rightp.next = dumpy.next
            dumpy.next = rightp
            rightp = tmp
        right = dumpy.next

        #回文判断
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    nums = "1,2,3,2,1"
    head = stringToListNode(nums)
    sol = Solution()
    result = sol.isPalindrome(head)
    print(result)
