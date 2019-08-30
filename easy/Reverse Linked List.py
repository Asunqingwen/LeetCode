# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 9:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse Linked List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

企业：爱奇艺 网易 Airbnb 大疆 快手 趣头条 地平线 美菜 网易游戏 支付宝 谷歌 优步 苹果 滴滴 小米 蚂蚁金服 薪人薪事 字节跳动 腾讯 阿里巴巴 百度 Facebook Adobe 瓜子二手车 Bloomberg 58 华为
标签：链表
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


def reverseList(head: ListNode) -> ListNode:
	if not head:
		return head
	tail = head.next
	head.next = None
	while tail:
		temp = tail.next
		tail.next = head
		head = tail
		tail = temp
	return head


def reverseList1(head: ListNode) -> ListNode:
	if not head or not head.next:
		return head
	new_h = reverseList1(head.next)
	head.next.next = head
	head.next = None
	return new_h


if __name__ == '__main__':
	input = "1,2,3,4,5"
	head = stringToListNode(input)
	head = reverseList1(head)
	result = listNodeToString(head)
	print(result)
