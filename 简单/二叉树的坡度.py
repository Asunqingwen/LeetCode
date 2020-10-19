"""
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

 

示例：

输入：
         1
       /   \
      2     3
输出：1
解释：
结点 2 的坡度: 0
结点 3 的坡度: 0
结点 1 的坡度: |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
 

提示：

任何子树的结点的和不会超过 32 位整数的范围。
坡度的值不会超过 32 位整数的范围。
"""
from Tree import TreeNode, stringToTreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res

        def dfs(node):
            if node is None:
                return 0
            left_sum = dfs(node.left) if node.left else 0
            right_sum = dfs(node.right) if node.right else 0
            nonlocal res
            res += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        left_sum = dfs(root.left) if root.left else 0
        right_sum = dfs(root.right) if root.right else 0
        res += abs(left_sum - right_sum)
        return res


if __name__ == '__main__':
    nums = '1,2,3'
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.findTilt(root))
