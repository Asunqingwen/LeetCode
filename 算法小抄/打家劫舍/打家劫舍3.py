"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""
from Tree import TreeNode, stringToTreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(node: TreeNode):
            if not node:
                # res[0]不抢root得到的最大钱数，res[1]抢root得到的最大钱数
                return [0, 0]
            rob_left = dp(node.left)
            rob_right = dp(node.right)
            # 不抢root,下一家可抢可不抢
            not_rob = max(rob_left[0], rob_left[1]) + max(rob_right[0], rob_right[1])
            # 抢root
            rob = node.val + rob_left[0] + rob_right[0]
            return [not_rob, rob]

        res = dp(root)
        return max(res[0], res[1])


if __name__ == '__main__':
    nums = "3,2,3,null,3,null,1"
    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.rob(root)
    print(result)
