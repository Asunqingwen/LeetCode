"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

 

示例 1：


输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。
示例 2：


输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。
 

提示：

树中节点数目在范围 [1, 25] 内
1 <= Node.val <= 231 - 1
对于树中每个节点 root.val == min(root.left.val, root.right.val)
"""
from Tree import TreeNode, stringToTreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = -1

        def dfs(node):
            nonlocal res
            if node is None:
                return
            # 如果左右子树值不相等，则第二小值为左右子树中较大的值
            if node.left is not None and node.left.val != node.right.val:
                bigger = max(node.left.val, node.right.val)
                res = bigger if res == -1 else min(res, bigger)
                # 将左右子树中较小值的树递归，查找更小的第二小值
                dfs(node.left if node.left.val < node.right.val else node.right)
            # 如果左右子树相等或者为空，分别递归
            else:
                dfs(node.left)
                dfs(node.right)
            return

        dfs(root)
        return res


if __name__ == '__main__':
    nums = "2,2,5,null,null,5,7"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.findSecondMinimumValue(root))
