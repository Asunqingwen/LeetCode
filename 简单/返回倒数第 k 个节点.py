'''
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：

给定的 k 保证是有效的。
'''
from LinkList import stringToListNode, ListNode


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        p = head
        for _ in range(k):
            p = p.next
        while p:
            head = head.next
            p = p.next
        return head.val


if __name__ == '__main__':
    nums = "1,2,3,4,5"
    k = 2
    head = stringToListNode(nums)
    sol = Solution()
    print(sol.kthToLast(head, k))
