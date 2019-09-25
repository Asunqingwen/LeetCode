# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 0025 15:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Linked List Cycle.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
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


def hasCycle(head):
	if not head:
		return False
	f, s = head, head
	while s.next and s.next.next:
		f = f.next
		s = s.next.next
		if f == s:
			return True
	return False


if __name__ == '__main__':
	input = [3, 2, 0, -4]
	head = listToListNode(input)
	result = hasCycle(head)
	print(result)
