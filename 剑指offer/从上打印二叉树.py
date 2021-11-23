from typing import List

from Tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nodes = [root]
        res = []
        while nodes:
            node = nodes.pop(0)
            res.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return res
