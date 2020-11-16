'''
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：



输入：[1,1,1,1,1,null,1]
输出：true
示例 2：



输入：[2,2,2,5,2]
输出：false
 

提示：

给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。
'''
from Tree import stringToTreeNode, TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_bool = self.isUnivalTree(root.left)
        if root.left:
            left_bool = left_bool and root.val == root.left.val
        right_bool = self.isUnivalTree(root.right)
        if root.right:
            right_bool = right_bool and root.val == root.right.val
        return left_bool and right_bool


if __name__ == '__main__':
    nums = "2,2,2,5,2"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.isUnivalTree(root))
