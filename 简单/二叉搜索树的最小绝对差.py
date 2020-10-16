"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
"""
import math

from Tree import TreeNode, stringToTreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []

        def dfs(node):
            if node is None:
                return
            if node.left:
                dfs(node.left)
            nums.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)

        return min([nums[i] - nums[i - 1] for i in range(1, len(nums))])


if __name__ == '__main__':
    nums = "4,2,6,1,3,null,null"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.getMinimumDifference(root))
