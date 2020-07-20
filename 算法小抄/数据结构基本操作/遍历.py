from typing import List


# 基本的单链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 基本二叉树节点，对比基本单链表节点结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 基本N叉树节点，对比基本二叉树节点结构
class TreeNodes:
    def __init__(self, x):
        self.val = x
        self.children = []


class traverse():
    def arrTraverse(self, arrs: List):
        """
        数组遍历框架
        :return:
        """
        for arr in arrs:
            print(arr)

    def listTraverse1(self, head: ListNode):
        """
        链表循环遍历
        :param head:
        :return:
        """
        p = head
        while p:
            print(p.val)
            p = p.next

    def listTraverse2(self, head: ListNode):
        """
        链表递归遍历
        :param head:
        :return:
        """
        print(head.val)
        self.listTraverse2(head.next)

    def treeTraverse(self, root: TreeNode):
        """
        二叉树递归先序遍历
        :return:
        """
        print(root.val)
        self.treeTraverse(root.left)
        self.treeTraverse(root.right)

    def treesTraverse(self, root: TreeNodes):
        """
        N叉树递归先序遍历
        :return:
        """
        print(root.val)
        for child in root.children:
            self.treesTraverse(child)

    def graphTraverse(self):
        """
        图的递归遍历，和N叉树的遍历类似，只是遍历过的节点需要用boolean变量标志，因为图存在环
        :return:
        """
        pass
