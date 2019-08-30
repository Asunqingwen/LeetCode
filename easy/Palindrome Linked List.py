# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 10:30
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Palindrome Linked List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
企业：字节跳动 阿里巴巴 Adobe 小米 百度 微软 优步 苹果 海康威视 滴滴 今日头条 网易 腾讯 IXL
标签：链表 双指针
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def stringToListNode(input):
	input = input.split(',')
	dummyRoot = ListNode(0)
	ptr = dummyRoot
	for number in input:
		ptr.next = ListNode(number)
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


def isPalindrome(head: ListNode) -> bool:
	if not head or not head.next:
		return True
	slow, fast, pre, prepre = head, head.next, None, None
	while fast and fast.next:
		pre = slow
		slow = slow.next
		fast = fast.next.next
		pre.next = prepre
		prepre = pre
	p2 = slow.next
	slow.next = pre
	p1 = slow.next if not fast else slow
	while p1:
		if p1.val != p2.val:
			return False
		p1 = p1.next
		p2 = p2.next
	return True


if __name__ == '__main__':
	input = "1,2,3,4,5,4,3,2,1"
	head = stringToListNode(input)
	result = isPalindrome(head)
	print(result)
