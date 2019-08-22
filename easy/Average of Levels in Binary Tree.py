# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 0022 11:58
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Average of Levels in Binary Tree.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
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


def averageOfLevels(root: TreeNode) -> List[float]:
	if not root:
		return []
	res_list = []
	tra_list = [root]

	while tra_list:
		cur_val = 0
		next_level = []
		for node in tra_list:
			cur_val += node.val

			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)

		res_list.append(cur_val / len(tra_list))
		tra_list = next_level
	return res_list


if __name__ == '__main__':
	input = "3,9,20,null,null,15,7"
	root = stringToTreeNode(input)
	output = averageOfLevels(root)
	print(output)
