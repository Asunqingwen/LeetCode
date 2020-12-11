'''
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''
from Tree import TreeNode, stringToTreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def helper(node: TreeNode):
            if not node:
                return None
            helper(node.right)
            if self.k == 0:
                return None
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            helper(node.left)

        self.k = k
        helper(root)
        return self.res


if __name__ == '__main__':
    nums = "3,1,4,null,2"
    k = 1
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.kthLargest(root, k))
