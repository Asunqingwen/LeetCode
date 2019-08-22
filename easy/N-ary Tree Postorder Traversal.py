# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 0022 9:11
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: N-ary Tree Postorder Traversal.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

# Definition for a Node.

"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].

 
Note:

Recursive solution is trivial, could you do it iteratively?
"""

from typing import List


class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children


def postorder(root: 'Node') -> List[int]:
	res_list = []
	pre_stack = [root]
	while pre_stack:
		node = pre_stack.pop()
		if node:
			res_list.append(node.val)
			if node.children:
				for child in node.children:
					pre_stack.append(child)
	return res_list[::-1]


if __name__ == '__main__':
	input = Node(1, 1)
	output = postorder(input)
	print(output)
