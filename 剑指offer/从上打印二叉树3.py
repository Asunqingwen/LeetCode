from typing import List

from Tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        nodes = [root]
        flag = True
        while nodes:
            val = []
            flag = not flag
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                val.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if flag:
                val = val[::-1]
            res.append(val)
        return res
