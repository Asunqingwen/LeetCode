'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''
from typing import List

from Tree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)

            # 右子树结点个数
            index = indexs[val]
            root.right = helper(index + 1, inorder_right)
            root.left = help(inorder_left, index - 1)
            return root

        indexs = {v: i for i, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    sol = Solution()
    sol.buildTree(inorder, postorder)
