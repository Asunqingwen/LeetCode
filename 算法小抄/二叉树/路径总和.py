"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def dfs(node, sum):
            if not node:
                return False
            elif sum - node.val == 0 and (not node.left and not node.right):
                return True
            return dfs(node.left, sum - node.val) or dfs(node.right, sum - node.val)

        return dfs(root, sum)

    def hasPathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        queue = [(root, sum)]
        while queue:
            node, path = queue.pop(0)
            if path - node.val == 0 and (not node.left and not node.right):
                return True
            if node.left:
                queue.append((node.left, path - node.val))
            if node.right:
                queue.append((node.right, path - node.val))
        return False


if __name__ == '__main__':
    nums = "1,2,2,null,3,null,3"
    sum = 22
    from Tree import stringToTreeNode

    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.hasPathSum(root, sum)
    print(result)
