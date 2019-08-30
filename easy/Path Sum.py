# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 0022 15:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Path Sum.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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


def pathSum(root: TreeNode, sum1: int) ->bool:
	if not root:
		return False
	tra_list = [[root, [root.val]]]

	while tra_list:
		root = tra_list.pop(0)
		if not root[0].left and not root[0].right:
			if sum(root[1]) == sum1:
				return True
		else:
			if root[0].left:
				path = []
				path.extend(root[1])
				path.append(root[0].left.val)
				tra_list.append([root[0].left, path])
			if root[0].right:
				path = []
				path.extend(root[1])
				path.append(root[0].right.val)
				tra_list.append([root[0].right, path])
	return False



if __name__ == '__main__':
	input = "5,4,8,11,null,13,4,7,2,null,null,5,1"
	root = stringToTreeNode(input)
	sum1 = 22
	output = pathSum(root, sum1)
	print(output)

