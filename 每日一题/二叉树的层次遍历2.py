"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""
from typing import List

from Tree import *


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        num = [root]
        result.append([root.val])
        while True:
            temp = []
            count = []
            while num:
                node = num.pop(0)
                if node.left:
                    temp.append(node.left)
                    count.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    count.append(node.right.val)
            if not temp:
                break
            num = temp[:]
            result.append(count)
        return result[::-1]


if __name__ == '__main__':
    nums = "3,9,20,2,3,15,7"
    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.levelOrder(root)
    print(result)
