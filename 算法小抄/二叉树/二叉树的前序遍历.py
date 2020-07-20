class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root):
            if not root:
                return None
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        res = []
        helper(root)
        return res

    def preorderTraversal1(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            # 保持最左在栈顶
            if node.left:
                stack.append(node.left)
        return res
