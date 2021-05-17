'''
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

 

示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
 

提示：

二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。
'''
from Tree import TreeNode, stringToTreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def helper(node: TreeNode, depth: int, parent: TreeNode):
            if not node:
                return
            nonlocal x_depth, y_depth, x_parent, y_parent, x_found, y_found
            if node.val == x:
                x_found = True
                x_depth = depth
                x_parent = parent
            elif node.val == y:
                y_found = True
                y_depth = depth
                y_parent = parent
            helper(node.left, depth + 1, node)
            if x_found and y_found:
                return
            helper(node.right, depth + 1, node)
            return

        x_depth, x_parent, x_found = 0, 0, False
        y_depth, y_parent, y_found = 0, 0, False
        helper(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent


if __name__ == '__main__':
    nums = "1,2,3,null,4"
    root = stringToTreeNode(nums)
    x = 2
    y = 3
    sol = Solution()
    print(sol.isCousins(root, x, y))
