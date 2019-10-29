# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 0028 10:45
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Remove Zero Sum Consecutive Nodes from Linked List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
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


def removeZeroSumSublists(head: ListNode) -> ListNode:
	# 前缀和
	prefix_sum = {}
	dumpy = ListNode(0)
	dumpy.next = head
	p = dumpy
	sum = 0
	prefix_sum[0] = p
	while p.next:
		p = p.next
		sum += p.val
		if sum in prefix_sum:
			tmp_node = prefix_sum[sum].next
			prefix_sum[sum].next = p.next
			temp_sum = sum
			while tmp_node != p:
				temp_sum += tmp_node.val
				prefix_sum.pop(temp_sum)
				tmp_node = tmp_node.next
		else:
			prefix_sum[sum] = p
	return dumpy.next

if __name__ == '__main__':
	input = "1,-1"
	head = stringToListNode(input)
	result = removeZeroSumSublists(head)
	result = listNodeToString(result)
	print(result)
