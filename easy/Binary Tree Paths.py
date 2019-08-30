# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 0022 14:16
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Binary Tree Paths.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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


def binaryTreePaths(root: TreeNode) -> List[str]:
	if not root:
		return []
	res_list = []
	tra_list = [[root, [str(root.val)]]]

	while tra_list:
		root = tra_list.pop(0)
		if not root[0].left and not root[0].right:
			res_list.append(root[1])
		else:
			if root[0].left:
				path = []
				path.extend(root[1])
				path.append(str(root[0].left.val))
				tra_list.append([root[0].left, path])
			if root[0].right:
				path = []
				path.extend(root[1])
				path.append(str(root[0].right.val))
				tra_list.append([root[0].right, path])

	return ['->'.join(r) for r in res_list]


if __name__ == '__main__':
	input = "1,2"
	root = stringToTreeNode(input)
	output = binaryTreePaths(root)
	print(output)
