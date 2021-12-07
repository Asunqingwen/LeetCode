from Tree import Node


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            if not node:
                return None
            dfs(node.left)  # 遍历左节点
            node.left = self.pre  # 当前节点左指针指向前一个节点
            if self.pre:
                self.pre.right = node  # 前一个节点右指针指向当前节点
            else:
                self.head = node  # 初始化头结点
            self.pre = node  # 指针后移，指向当前节点
            dfs(node.right)  # 遍历右节点

        if not root:
            return None
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head  # 头结点和尾节点相互指
        return self.head
