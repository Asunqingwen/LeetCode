# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 16:06
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: N-ary Tree Preorder Traversal.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

 

Note:

Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
from typing import List


class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children


def preorder(root: 'Node') -> List[int]:
	res_list = []
	pre_stack = [root]
	while pre_stack:
		root = pre_stack.pop()
		if root:
			res_list.append(root.val)
			if root.children:
				for child in root.children[::-1]:
					pre_stack.append(child)
	return res_list


if __name__ == '__main__':
	input = Node(1, 1)
	output = preorder(input)
	print(output)
