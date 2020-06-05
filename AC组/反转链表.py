"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000
"""
from LinkList import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preHead = ListNode(-1)
        while head:
            ptr = head.next
            head.next = preHead.next
            preHead.next = head
            head = ptr
        return preHead.next


if __name__ == '__main__':
    input1 = "1, 2,3,4,5"
    head = stringToListNode(input1)
    sol = Solution()
    head = sol.reverseList(head)
    print(listNodeToString(head))
