# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 11:58
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Intersection of Two Linked Lists.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
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


def getIntersectionNode(headA, headB):
	"""
	:type head1, head1: ListNode
	:rtype: ListNode
	"""
	pA, pB = headA, headB
	lenA, lenB = 0, 0
	while pA:
		lenA += 1
		pA = pA.next
	while pB:
		lenB += 1
		pB = pB.next
	pA, pB = headA, headB
	if lenA < lenB:
		for _ in range(lenB - lenA):
			pB = pB.next
	else:
		for _ in range(lenA - lenB):
			pA = pA.next
	while pA and pB:
		if pA == pB:
			return pA
		pA = pA.next
		pB = pB.next
	return None


def getIntersectionNode2(headA, headB):
	pA, pB = headA, headB
	while pA != pB:
		pA = headB if pA is None else pA.next
		pB = headA if pB is None else pB.next
	return pA


if __name__ == '__main__':
	listA = [4, 1, 8, 4, 5]
	listB = [5, 0, 1, 8, 4, 5]
	headA = listToListNode(listA)
	headB = listToListNode(listB)
	result = getIntersectionNode(headA, headB)
	printListNode(result)
