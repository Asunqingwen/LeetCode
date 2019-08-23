# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0023 15:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximum Depth of N-ary Tree.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:
We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""


class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children


def maxDepth(root: 'Node') -> int:
	if not root:
		return 0
	node_depth_dict = [[root, 1]]
	depth = 0
	while node_depth_dict:
		node_depth = node_depth_dict.pop(0)
		root = node_depth[0]
		curr_depth = node_depth[1]
		depth = max(depth, curr_depth)
		if root.children:
			for child in root.children:
				node_depth_dict.append([child, curr_depth + 1])
	return depth


if __name__ == '__main__':
	input = Node(1, 1)
	output = maxDepth(input)
	print(output)
