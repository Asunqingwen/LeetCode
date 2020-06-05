"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[3,9,20,null,null,15,7]
"""
from typing import List

from Tree import *


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        num = [root]
        result.append(root.val)
        while num:
            node = num.pop(0)
            if node.left:
                num.append(node.left)
                result.append(node.left.val)
            if node.right:
                num.append(node.right)
                result.append(node.right.val)
        return result


if __name__ == '__main__':
    nums = "3,9,20,null,null,15,7"
    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.levelOrder(root)
    print(result)
