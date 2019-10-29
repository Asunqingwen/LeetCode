# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 0028 13:50
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Odd Even Linked List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
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


def oddEvenList(head: ListNode) -> ListNode:
	if not head or not head.next or not head.next.next:
		return head
	p1, p2, p3 = head, head.next, head.next
	while p2 and p2.next:
		p1.next = p2.next
		p2.next = p2.next.next
		p1.next.next = p3
		p1 = p1.next
		p2 = p2.next
	return head


if __name__ == '__main__':
	input = "2,1,3,5,6,4,7"
	head = stringToListNode(input)
	result = oddEvenList(head)
	result = listNodeToString(result)
	print(result)
