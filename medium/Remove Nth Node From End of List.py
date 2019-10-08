# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 14:14
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Remove Nth Node From End of List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
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


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
	p1, p2 = head, head
	for _ in range(n):
		p2 = p2.next
	if not p2:
		return p1.next
	while p2.next:
		p1, p2 = p1.next, p2.next
	p1.next = p1.next.next
	return head


if __name__ == '__main__':
	input = [1, 2, 3, 4, 5]
	n = 2
	head = listToListNode(input)
	result = removeNthFromEnd(head, n)
	printListNode(result)
