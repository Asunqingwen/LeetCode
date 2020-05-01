"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from LinkList import ListNode, listNodeToString, stringToListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return prehead.next


if __name__ == '__main__':
    input1 = "1, 2, 4"
    input2 = "1, 3, 4"
    l1 = stringToListNode(input1)
    l2 = stringToListNode(input2)
    sol = Solution()
    l = sol.mergeTwoLists(l1, l2)
    print(listNodeToString(l))
