from Tree import TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        def recur(node: TreeNode):
            node.left, node.right = node.right, node.left
            if node.left:
                recur(node.left)
            if node.right:
                recur(node.right)
            return node

        return recur(root)
