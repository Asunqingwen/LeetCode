"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
"""
from Tree import TreeNode, stringToTreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        sums = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            if k - node.val in sums:
                return True
            sums.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


if __name__ == '__main__':
    nums = "5,3,6,2,4,null,7"
    k = 28
    root = stringToTreeNode(nums)
    sol = Solution()
    result = sol.findTarget(root, k)
    print(result)
