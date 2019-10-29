# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 0029 9:42
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Split Linked List in Parts.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""
import json
from typing import List


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


def splitListToParts(root: ListNode, k: int) -> List[ListNode]:
	res = []
	length = 0
	p = root
	while p:
		length += 1
		p = p.next
	part = length // k
	extra = length % k
	p = root
	for i in range(k):
		count = 0
		if extra > 0:
			count = -1
		tmp_head = ListNode(0)
		tmp_p = tmp_head
		while count < part:
			node = ListNode(p.val)
			tmp_p.next = node
			p = p.next
			tmp_p = tmp_p.next
			count += 1
		res.append(tmp_head.next)
		extra -= 1
	return res


if __name__ == '__main__':
	input = "1,2,3,4,5,6,7"
	k = 3
	root = stringToListNode(input)
	result = splitListToParts(root, k)
