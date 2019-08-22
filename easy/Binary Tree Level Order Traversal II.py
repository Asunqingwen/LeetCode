# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 0022 11:44
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Binary Tree Level Order Traversal II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
from typing import List


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def stringToTreeNode(input):
	input = input.strip()
	if not input:
		return None

	inputValues = [s.strip() for s in input.split(',')]
	root = TreeNode(int(inputValues[0]))
	nodeQueue = [root]
	front = 0
	index = 1
	while index < len(inputValues):
		node = nodeQueue[front]
		front = front + 1

		item = inputValues[index]
		index = index + 1
		if item != "null":
			leftNumber = int(item)
			node.left = TreeNode(leftNumber)
			nodeQueue.append(node.left)

		if index >= len(inputValues):
			break

		item = inputValues[index]
		index = index + 1
		if item != "null":
			rightNumber = int(item)
			node.right = TreeNode(rightNumber)
			nodeQueue.append(node.right)
	return root


def treeNodeToString(root):
	if not root:
		return "[]"
	output = ""
	queue = [root]
	current = 0
	while current != len(queue):
		node = queue[current]
		current = current + 1

		if not node:
			output += "null, "
			continue

		output += str(node.val) + ", "
		queue.append(node.left)
		queue.append(node.right)
	return "[" + output + "]"


def levelOrderBottom(root: TreeNode) -> List[List[int]]:
	if not root:
		return []
	res_list = []
	tra_list = [root]

	while tra_list:
		cur_val = []
		next_level = []
		for node in tra_list:
			cur_val.append(node.val)

			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)

		res_list.append(cur_val)
		tra_list = next_level
	return res_list[::-1]


if __name__ == '__main__':
	input = "3,9,20,null,null,15,7"
	root = stringToTreeNode(input)
	output = levelOrderBottom(root)
	print(output)
