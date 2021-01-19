'''
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
from Tree import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node:TreeNode):
            if not node:
                return node
            if not node.left:
                node.right = dfs(node.right)
                return node
            tmp = node.right
            node.right = dfs(node.left)
            node.left = None
            tmp_f = node.right
            while tmp_f.right:
                tmp_f = tmp_f.right
            tmp_f.right = dfs(tmp)
            return node
        dfs(root)
