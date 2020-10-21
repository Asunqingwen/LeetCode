"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 

提示：

节点值的范围在32位有符号整数范围内。
通过次数48,630提交次数70,779
"""
from typing import List

from Tree import TreeNode, stringToTreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if root is None:
            return res
        ans = [root]

        while True:
            tmp = []
            count = 0
            sum_ = 0
            while ans:
                node = ans.pop(0)
                sum_ += node.val
                count += 1
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            if count == 0:
                res.append(0)
            else:
                res.append(sum_ / count)
            if not tmp:
                break
            ans[:] = tmp[:]

        return res


if __name__ == '__main__':
    nums = "3,9,20,15,7"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.averageOfLevels(root))
