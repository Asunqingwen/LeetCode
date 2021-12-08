from Tree import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.right)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            dfs(node.left)

        self.k = k
        self.res = 0
        dfs(root)
        return self.res
