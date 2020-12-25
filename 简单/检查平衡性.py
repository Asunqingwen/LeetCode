'''
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。
'''
from Tree import TreeNode, stringToTreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(node: TreeNode):
            if not node:
                return 0
            ldepth = helper(node.left)
            rdepth = helper(node.right)
            if ldepth == -1 or rdepth == -1 or abs(ldepth - rdepth) > 1:
                return -1
            return max(ldepth, rdepth) + 1

        return helper(root) >= 0


if __name__ == '__main__':
    nums = "1,2,2,3,3,null,null,4,4"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.isBalanced(root))
