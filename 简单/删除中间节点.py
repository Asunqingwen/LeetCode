'''
实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。

 

示例：

输入：单向链表a->b->c->d->e->f中的节点c
结果：不返回任何数据，但该链表变为a->b->d->e->f
'''
from LinkList import ListNode, stringToListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.next = node.next.next
        node.val = node.next.val

if __name__ == '__main__':
    str_ = "a,b,c,d,e,f"
    node = stringToListNode(str_)
    sol = Solution()
    sol.deleteNode(node)
