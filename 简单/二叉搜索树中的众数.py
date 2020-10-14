'''
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
'''
from typing import List

from Tree import TreeNode, stringToTreeNode
from collections import defaultdict


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        hashMap = defaultdict(int)

        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            hashMap[node.val] += 1
            if node.right:
                dfs(node.right)

        dfs(root)
        max_count = max(hashMap.values())

        for k, v in hashMap.items():
            if v == max_count:
                res.append(k)
        return res


if __name__ == '__main__':
    nums = "2147483647"
    root = stringToTreeNode(nums)
    sol = Solution()
    print(sol.findMode(root))
