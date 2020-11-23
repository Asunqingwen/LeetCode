'''
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 32 位 整数。

 

示例 1：


输入：root = [1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
示例 2：

输入：root = [0]
输出：0
示例 3：

输入：root = [1]
输出：1
示例 4：

输入：root = [1,1]
输出：3
 

提示：

树中的结点数介于 1 和 1000 之间。
Node.val 为 0 或 1 。
'''
from Tree import TreeNode, stringToTreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, sum_=0):
            if not node.left and not node.right:
                nonlocal res
                sum_ = (sum_ << 1) + node.val
                res += sum_
                return
            sum_ = (sum_ << 1) + node.val
            if node.left:
                dfs(node.left, sum_)
            if node.right:
                dfs(node.right, sum_)
            return

        res = 0
        dfs(root)
        return res


if __name__ == '__main__':
    nums = "1,0,1,0,1,0,1"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.sumRootToLeaf(root))
