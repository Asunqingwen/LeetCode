"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""
import math

from Tree import TreeNode, stringToTreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        res = math.inf
        while queue:
            node, depth = queue.pop(-1)
            if not node.left and not node.right:
                res = min(depth, res)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return res


if __name__ == '__main__':
    nums = "3,9,20,null,null,15,7"
    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.minDepth(root)
    print(result)
