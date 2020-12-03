'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000
'''
from typing import List

from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]


if __name__ == '__main__':
    nums = "1,2,3,4,5"
    head = stringToListNode(nums)
    sol = Solution()
    print(listNodeToString(sol.reversePrint(head)))
