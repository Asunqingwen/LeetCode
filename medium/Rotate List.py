# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 0029 10:26
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rotate List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
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
		ptr.next = ListNode(int(number))
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


def rotateRight(head: ListNode, k: int) -> ListNode:
	p1 = head
	length = 0
	while p1:
		length += 1
		p1 = p1.next
	if length <= 1 or k == 0:
		return head
	k %= length
	p1, p2 = head, head
	for i in range(k):
		p2 = p2.next
	for i in range(length - k):
		if not p1.next:
			p1.next = head
		if not p2.next:
			p2.next = head
		p1 = p1.next
		p2 = p2.next
	head = p1
	for i in range(length - 1):
		p1 = p1.next
	p1.next = None
	return head


if __name__ == '__main__':
	input = "1,2"
	k = 0
	head = stringToListNode(input)
	result = rotateRight(head, k)
	result = listNodeToString(result)
	print(result)
