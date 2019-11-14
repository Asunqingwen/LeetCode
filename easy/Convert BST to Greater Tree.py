# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 0014 9:39
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Convert BST to Greater Tree.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
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


def convertBST(root: TreeNode) -> TreeNode:
	if not root:
		return root
	ans = []

	def helper(root):
		if root.right:
			helper(root.right)
		ans.append(root)
		if root.left:
			helper(root.left)

	helper(root)
	pre_sum = 0
	while ans:
		tmp = ans.pop(0)
		tmp.val += pre_sum
		pre_sum = tmp.val
	return root


if __name__ == '__main__':
	input = "5,2,13"
	root = stringToTreeNode(input)
	root = convertBST(root)
	result = treeNodeToString(root)
	print(result)
