# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 0022 10:51
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: N-ary Tree Level Order Traversal.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
 

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

from typing import List


class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children


def levelOrder(root: 'Node') -> List[List[int]]:
	res_list = []
	pre_stack = [[root]]
	while pre_stack:
		root = pre_stack.pop(0)
		child_list = []
		val_list = []
		for r in root:
			if r:
				val_list.append(r.val)
				if r.children:
					child_list.extend(r.children)
		if len(child_list):
			pre_stack.append(child_list)
		if len(val_list):
			res_list.append(val_list)

	return res_list


if __name__ == '__main__':
	input = Node(1, 1)
	output = levelOrder(input)
	print(output)
