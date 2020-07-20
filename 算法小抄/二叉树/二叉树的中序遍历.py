class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root):
            if not root:
                return None
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        res = []
        helper(root)
        return res

    def inorderTraversal1(self, root):
        res = []
        if not root:
            return res
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                # 最左结点
                root = root.left
            # 开始遍历
            if stack:
                node = stack.pop()
                res.append(node.val)
                # 对某个右节点进行最左结点获取
                root = root.right
        return res
