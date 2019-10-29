# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 0028 9:46
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Remove Duplicates from Sorted List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
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
	if not head:
		return head
	p1, p2 = head, head
	while p2.next:
		p2 = p2.next
		if p2.val == p1.val:
			p1.next = p2.next
		else:
			p1 = p2
	return head


if __name__ == '__main__':
	input = ""
	head = stringToListNode(input)
	result = deleteDuplicates(head)
	result = listNodeToString(result)
	print(result)
