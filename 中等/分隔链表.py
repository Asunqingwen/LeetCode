"""
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

示例 1：

输入:
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
解释:
输入输出各部分都应该是链表，而不是数组。
例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.next.next.next = null。
第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
示例 2：

输入:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释:
输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
 

提示:

root 的长度范围： [0, 1000].
输入的每个节点的大小范围：[0, 999].
k 的取值范围： [1, 50].
"""
from typing import List

from LinkList import ListNode, stringToListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return []
        if k == 1:
            return [root]
        lenr = 0
        p = root
        while p:
            lenr += 1
            p = p.next
        div = lenr // k
        mod = lenr % k
        res = [None] * k
        i = 0
        # 长度多1的结点
        while i < mod:
            p = root
            for _ in range(div):
                root = root.next
            # p到root之间的结点，即为一段
            res[i] = p
            p = root
            root = root.next
            p.next = None
            i += 1
        # 长度正常的结点
        while i < k:
            p = root
            if div == 0:
                break
            for _ in range(div - 1):
                root = root.next
            res[i] = p
            p = root
            root = root.next
            p.next = None
            i += 1
        return res


if __name__ == '__main__':
    nums = "1,2,3"
    k = 5
    root = stringToListNode(nums)
    sol = Solution()
    sol.splitListToParts(root, k)
