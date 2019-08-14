# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 10:38
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Remove Linked List Elements.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def removeElements(head: ListNode, val: int) -> ListNode:
	tail = ListNode(-1)
	tail.next = head
	pre = tail
	while pre.next is not None:
		if pre.next.val == val:
			pre.next = pre.next.next
		else:
			pre = pre.next
	return tail.next

if __name__ == '__main__':
	val = []
	head = ListNode(1)
	tail = head
	val = val[1:]
	for i in val:
		node = ListNode(i)
		tail.next = node
		tail = node
	val = 1
	removeElements(head, val)
	while head is not None:
		print(head.val)
		head = head.next
