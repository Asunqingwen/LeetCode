class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root):
            if not root:
                return None
            helper(root.left)
            helper(root.right)
            res.append(root.val)

        res = []
        helper(root)
        return res

    def postorderTraversal1(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        # 后序遍历是左右根，倒置就是根右左，先序遍历是根左右，将左右调换，就能将后序遍历变为先序遍历了
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]


if __name__ == '__main__':
    nums = "1,2,3,4,5,6,7,8,9"
    from Tree import stringToTreeNode

    root = stringToTreeNode(nums)
    sol = Solution()
    sol.postorderTraversal1(root)
