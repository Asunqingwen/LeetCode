'''
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
'''
from Tree import TreeNode, stringToTreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0

        def allSum(root):
            if not root: return []  # 递归终点
            possible = [root.val]
            if root.val == sum: self.ans += 1  # 根 == sum
            left = allSum(root.left)
            right = allSum(root.right)
            for i in left:
                temp = root.val + i  # 根 + 左可能值
                possible.append(temp)
                if temp == sum: self.ans += 1
            for i in right:
                temp = root.val + i  # 根 + 右可能值
                possible.append(temp)
                if temp == sum: self.ans += 1
            return possible

        allSum(root)
        return self.ans


if __name__ == '__main__':
    nums = "10,5,-3,3,2,null,11,3,-2,null,1"
    sum = 8
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.pathSum(root, sum))
