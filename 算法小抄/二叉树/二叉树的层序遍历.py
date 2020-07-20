class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        stack = [root]
        while True:
            count = []
            tmp = []
            while stack:
                node = stack.pop(0)
                count.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(count)
            if not tmp:
                break
            stack = tmp[:]
        return res


if __name__ == '__main__':
    nums = "3,9,20,null,null,15,7"
    from Tree import stringToTreeNode

    root = stringToTreeNode(nums)
    sol = Solution()
    sol.levelOrder(root)
