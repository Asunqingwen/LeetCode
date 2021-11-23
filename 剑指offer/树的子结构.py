from Tree import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
       if not B:
           return False
