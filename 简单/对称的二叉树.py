'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
'''
from Tree import TreeNode, stringToTreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(lnode: TreeNode, rnode: TreeNode):
            if not lnode and not rnode:
                return True
            elif not lnode or not rnode or lnode.val != rnode.val:
                return False
            return helper(lnode.left, rnode.right) and helper(lnode.right, rnode.left)

        return helper(root.left, root.right) if root else True


if __name__ == '__main__':
    nums = "1,2,2,3,4,4,3"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.isSymmetric(root))
