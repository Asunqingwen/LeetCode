'''
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

 

示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 

提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
'''
from Tree import TreeNode, stringToTreeNode
import math


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_ = -math.inf

        def dfs(node: TreeNode):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            self.max_ = max(self.max_, node.val + left_max + right_max)
            return max(0, left_max + node.val, right_max + node.val)

        dfs(root)
        return self.max_


if __name__ == '__main__':
    nums = "1,2,3"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.maxPathSum(root))
