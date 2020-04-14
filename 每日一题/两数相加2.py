"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
import json
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def stringToListNode(input):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class Solution:
    def listToStack(self, l: ListNode) -> List:
        list_stack = []
        while l:
            list_stack.append(l.val)
            l = l.next
        return list_stack

    def stackToList(self, l_stack: List) -> ListNode:
        dumpyRoot = ListNode(0)
        ptr = dumpyRoot.next
        for ls in l_stack:
            dumpyRoot.next = ListNode(ls)
            dumpyRoot.next.next = ptr
            ptr = dumpyRoot.next
        ptr = dumpyRoot.next
        return ptr

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stack = self.listToStack(l1)
        l2_stack = self.listToStack(l2)
        l_stack = []
        yu = 0
        while l1_stack and l2_stack:
            val1, val2 = l1_stack.pop(), l2_stack.pop()
            sum = val1 + val2 + yu
            add = sum % 10
            yu = sum // 10
            l_stack.append(add)
        while l1_stack:
            val1, val2 = l1_stack.pop(), yu
            sum = val1 + yu
            add = sum % 10
            yu = sum // 10
            l_stack.append(add)
            if yu == 0:
                l_stack.extend(l1_stack[::-1])
                break
        while l2_stack:
            val1, val2 = l2_stack.pop(), yu
            sum = val1 + yu
            add = sum % 10
            yu = sum // 10
            l_stack.append(add)
            if yu == 0:
                l_stack.extend(l2_stack[::-1])
                break
        if yu > 0:
            l_stack.append(yu)
        return self.stackToList(l_stack)


if __name__ == '__main__':
    str1 = [1]
    str2 = [9,9]
    l1 = stringToListNode(str1)
    l2 = stringToListNode(str2)
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print(listNodeToString(result))
