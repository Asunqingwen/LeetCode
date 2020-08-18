"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""
from Tree import TreeNode
from LinkList import ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        p = head
        length = 0
        # 链表长度
        while p:
            length += 1
            p = p.next

        def buildTree(left, right):
            if left > right:
                return None
            mid = (left + right) >> 1
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        return buildTree(0, length - 1)
