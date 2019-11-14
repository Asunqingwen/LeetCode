# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 0014 10:07
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Second Minimum Node In a Binary Tree.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
 

Example 2:

Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
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


def findSecondMinimumValue(root: TreeNode) -> int:
	min = [float('inf'), float('inf')]

	def helper(root):
		if root:
			if min[0] < root.val < min[1]:
				min[1] = root.val
			else:
				min[0] = root.val
			helper(root.left)
			helper(root.right)

	helper(root)
	if min[1] != float('inf'):
		return int(min[1])
	else:
		return -1


if __name__ == '__main__':
	input = "2,2,5,null,null,5,7"
	root = stringToTreeNode(input)
	result = findSecondMinimumValue(root)
	print(result)
