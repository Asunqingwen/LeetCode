# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 13:42
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Add Two Numbers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def listToListNode(data: list) -> ListNode:
	listRoot = ListNode(0)
	ptr = listRoot
	for d in data:
		ptr.next = ListNode(d)
		ptr = ptr.next

	ptr = listRoot.next
	return ptr


def printListNode(l: ListNode) -> None:
	p = l
	val_list = []
	while p:
		val_list.append(str(p.val))
		p = p.next
	print(' -> '.join(val_list))


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
	ptr1 = l1
	ptr2 = l2
	ptr_res = ListNode(0)
	ptr_curr = ptr_res
	add_bit = 0
	while ptr1 or ptr2:
		x = 0 if ptr1 is None else ptr1.val
		y = 0 if ptr2 is None else ptr2.val
		sum_val = x + y + add_bit
		add_bit = sum_val // 10
		ptr_curr.next = ListNode(sum_val % 10)
		ptr_curr = ptr_curr.next
		if ptr1 is not None:
			ptr1 = ptr1.next
		if ptr2 is not None:
			ptr2 = ptr2.next

	if add_bit > 0:
		ptr_curr.next = ListNode(add_bit)
	return ptr_res.next


if __name__ == '__main__':
	l1 = listToListNode([1])
	l2 = listToListNode([9, 9])
	l3 = addTwoNumbers(l1, l2)
	printListNode(l3)
