from Tree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def recur(left_node: TreeNode, right_node: TreeNode) -> bool:
            if not left_node and not right_node:
                return True
            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            return recur(left_node.left, right_node.right) and recur(left_node.right, right_node.left)

        return recur(root.left, root.right)
