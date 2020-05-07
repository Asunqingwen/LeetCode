"""
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。
"""
from Tree import TreeNode, stringToTreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSameTree(p, q):
            return (p == q) or (
                    p and q and p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right))

        if s is None:
            return False
        elif s.val == t.val and isSameTree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    s1 = "3,4,5,1,2,null,null"
    t1 = "4,1,2"
    s = stringToTreeNode(s1)
    t = stringToTreeNode(t1)
    sol = Solution()
    result = sol.isSubtree(s, t)
    print(result)
