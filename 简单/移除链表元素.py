"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 哨兵结点
        dumpy = ListNode(0)
        dumpy.next = head
        prev, curr = dumpy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dumpy.next


if __name__ == '__main__':
    nums = "1,2,3,6"
    val = 6
    head = stringToListNode(nums)
    sol = Solution()
    result = sol.removeElements(head, val)
    print(listNodeToString(result))
