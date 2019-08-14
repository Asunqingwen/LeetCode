# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 10:19
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Delete Node in a Linked List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def deleteNode(node: ListNode):
	node.val = node.next.val
	node.next = node.next.next


if __name__ == '__main__':
	val = [4, 5, 1, 9]
	head = ListNode(4)
	tail = head
	val = val[1:]
	for i in val:
		node = ListNode(i)
		tail.next = node
		tail = node
	node = ListNode(1)
	result = deleteNode(head)
	print(head)
