# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 14:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Merge Two Sorted Lists.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def stringToListNode(input):
	input = input.split(',')
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


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
	p1, p2 = l1, l2
	res = ListNode(0)
	p = res
	while p1 and p2:
		if p1.val < p2.val:
			temp = ListNode(p1.val)
			p.next = temp
			p1 = p1.next
			p = p.next
		else:
			temp = ListNode(p2.val)
			p.next = temp
			p2 = p2.next
			p = p.next
	while p1:
		temp = ListNode(p1.val)
		p.next = temp
		p1 = p1.next
		p = p.next
	while p2:
		temp = ListNode(p2.val)
		p.next = temp
		p2 = p2.next
		p = p.next
	return res.next


if __name__ == '__main__':
	input1 = ""
	input2 = ""
	root1 = stringToListNode(input1)
	root2 = stringToListNode(input2)
	result = mergeTwoLists(root1, root2)
	root = listNodeToString(result)
	print(root)
