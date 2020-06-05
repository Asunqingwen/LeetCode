"""
新建一个双向链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


def stringToListNode(input):
    input = input.split(',')
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        temp_node = ListNode(int(number))
        ptr.next = temp_node
        temp_node.pre = ptr
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