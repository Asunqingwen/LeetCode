'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 

示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
'''
from LinkList import ListNode, stringToListNode, listNodeToString


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            '''合并两个有序链表'''
            dummpy = ListNode(0)
            tmp, tmp1, tmp2 = dummpy, head1, head2
            while tmp1 and tmp2:
                if tmp1.val <= tmp2.val:
                    tmp.next = tmp1
                    tmp1 = tmp1.next
                else:
                    tmp.next = tmp2
                    tmp2 = tmp2.next
                tmp = tmp.next
            if tmp1:
                tmp.next = tmp1
            elif tmp2:
                tmp.next = tmp2
            return dummpy.next

        if not head:
            return head

        # 链表长度
        len_ = 0
        node = head
        while node:
            len_ += 1
            node = node.next

        dummpy = ListNode(0, head)
        # 初始子链表长度
        subLen = 1
        while subLen < len_:
            # 两两归并排序
            pre, curr = dummpy, dummpy.next
            while curr:
                # 第一个链表
                head1 = curr
                for _ in range(1, subLen):
                    if not curr.next:
                        break
                    curr = curr.next

                # 第二个链表
                head2, curr.next = curr.next, None
                curr = head2
                for _ in range(1, subLen):
                    if not curr or not curr.next:
                        break
                    curr = curr.next
                succ = None
                if curr:
                    succ, curr.next = curr.next, succ

                merged = merge(head1, head2)
                pre.next = merged
                while pre.next:
                    pre = pre.next
                curr = succ
            subLen <<= 1
        return dummpy.next


if __name__ == '__main__':
    nums = "4,2,1,3"
    head = stringToListNode(nums)
    sol = Solution()
    print(listNodeToString(sol.sortList(head)))
