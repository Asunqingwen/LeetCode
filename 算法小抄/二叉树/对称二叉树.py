"""
给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
"""
from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque()
        queue.extend([root, root])
        while queue:
            l, r = queue.popleft(), queue.popleft()
            if not l and not r:
                continue
            if (not l or not r) or (l.val != r.val):
                return False
            queue.extend([l.left, r.right])
            queue.extend([l.right, r.left])
        return True

    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(l, r):
            if not l and not r:
                return True
            if (not l or not r) or l.val != r.val:
                return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root, root)


if __name__ == '__main__':
    nums = "1,2,2,null,3,null,3"
    from Tree import stringToTreeNode

    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.isSymmetric1(root)
    print(result)
