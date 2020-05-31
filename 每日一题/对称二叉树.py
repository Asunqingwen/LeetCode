"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
"""
from collections import deque
from queue import SimpleQueue
from Tree import *


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        deque = SimpleQueue()
        deque.put(root)
        deque.put(root)
        while not deque.empty():
            l, r = deque.get(), deque.get()
            if not l and not r:
                continue
            if (not l or not r) or (l.val != r.val):
                return False
            deque.put(l.left)
            deque.put(r.right)

            deque.put(l.right)
            deque.put(r.left)
        return True

    def isSymmetric1(self, root: TreeNode) -> bool:
        queue = deque()
        queue.extend([root, root])
        while queue:
            l, r = queue.popleft(), queue.popleft()
            if not l and not r:
                continue
            if (not l or not r) or (l.val != r.val):
                return False
            queue.extend([l.left, r.right])
            queue.extend([l.right, r.left])
        return True


if __name__ == '__main__':
    s = "1,2,2,3,4,4,3"
    root = stringToTreeNode(s)
    sol = Solution()
    result = sol.isSymmetric1(root)
    print(result)
    test = deque()
    test.append(root)
