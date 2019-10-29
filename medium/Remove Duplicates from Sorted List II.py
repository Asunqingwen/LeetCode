# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 0028 9:58
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Remove Duplicates from Sorted List II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

import json


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def stringToIntegerList(input):
	return json.loads(input)


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


def deleteDuplicates(head: ListNode) -> ListNode:
	count = {}
	p = head
	while p:
		count[p.val] = count.get(p.val, 0) + 1
		p = p.next
	h = stringToListNode('')
	h.next = head
	p = h
	while h.next:
		if count[h.next.val] > 1:
			h.next = h.next.next
		else:
			h = h.next
	return p.next


if __name__ == '__main__':
	input = "1,2,3,3,4,4,5"
	head = stringToListNode(input)
	result = deleteDuplicates(head)
	result = listNodeToString(result)
	print(result)
