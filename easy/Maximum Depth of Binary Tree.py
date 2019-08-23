# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0023 15:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximum Depth of Binary Tree.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


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


def maxDepth(root: TreeNode) -> int:
	def getDepth(root: TreeNode) -> int:
		if not root:
			return 0
		res = max(getDepth(root.left), getDepth(root.right)) + 1
		return res

	return getDepth(root)


def maxDepth1(root: TreeNode) -> int:
	if not root:
		return 0
	node_depth_dict = [[root, 1]]
	depth = 0
	while node_depth_dict:
		node_depth = node_depth_dict.pop(0)
		root = node_depth[0]
		curr_depth = node_depth[1]
		if root:
			depth = max(depth, curr_depth)
			if root.left:
				node_depth_dict.append([root.left, curr_depth + 1])
			if root.right:
				node_depth_dict.append([root.right, curr_depth + 1])
	return depth


if __name__ == '__main__':
	input = "3,9,20,null,null,15,7,null,null,8,null"
	root = stringToTreeNode(input)
	output = maxDepth1(root)
	print(output)
