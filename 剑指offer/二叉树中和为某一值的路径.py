from typing import List
from Tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def dfs(node: TreeNode, sum_: int, tmp=None) -> None:
            if not node:
                return

            tmp.append(node.val)
            sum_ -= node.val
            if not node.left and not node.right and sum_ == 0:
                res.append(tmp[:])
            dfs(node.left, sum_, tmp)
            dfs(node.right, sum_, tmp)
            tmp.pop()
            return

        res = list()
        dfs(root, target, list())
        return res
