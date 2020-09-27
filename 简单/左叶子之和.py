"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""
from Tree import TreeNode, stringToTreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return None
            if node.left and not node.left.left and not node.left.right:
                self.res += node.left.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res


if __name__ == '__main__':
    nums = "3,9,20,null,null,null,7"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.sumOfLeftLeaves(root))
