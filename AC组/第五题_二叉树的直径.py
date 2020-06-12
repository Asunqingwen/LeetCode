"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

 

注意：两结点之间的路径长度是以它们之间边的数目表示。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Tree import TreeNode, stringToTreeNode


class Solution:
    def __init__(self):
        self.max_d = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(childNode: TreeNode) -> int:
            if not childNode:
                return 0
            left = depth(childNode.left)
            right = depth(childNode.right)
            self.max_d = max(left + right, self.max_d)
            return max(left, right) + 1  # 返回结点深度

        depth(root)
        return self.max_d


if __name__ == '__main__':
    nums = "1,2,3,4,5"
    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.diameterOfBinaryTree(root)
    print(result)
