"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""
from Tree import TreeNode


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            index = inorder_dict[val]

            # 后序遍历，所以先生成右子树
            # fist build right subtree
            root.right = helper(index + 1, in_right)
            # second build left subtree
            root.left = helper(in_left, index - 1)
            return root

        inorder_dict = {val: index for index, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    result = sol.buildTree(inorder, postorder)
    print(result)
