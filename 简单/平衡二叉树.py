"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""
from Tree import TreeNode, stringToTreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = 0

        def helper(root):
            if not root:
                return 0
            left_h = helper(root.left)
            if left_h == -1:
                return -1
            right_h = helper(root.right)
            if right_h == -1:
                return -1
            if abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1

        if root:
            res = helper(root)
        return res != -1


if __name__ == '__main__':
    nums1 = "1,2,2,3,3,null,null,4,4"
    root = stringToTreeNode(nums1)
    sol = Solution()
    result = sol.isBalanced(root)
    print(result)
