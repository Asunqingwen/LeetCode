# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 0016 10:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Range Sum of BST.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
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


def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
	res = 0

	def dfs(node):
		if node:
			if L <= node.val <= R:
				nonlocal res
				print(node.val)
				res += node.val
			if L < node.val:
				dfs(node.left)
			if node.val < R:
				dfs(node.right)

	dfs(root)
	return res


def rangeSumBST1(root: TreeNode, L: int, R: int) -> int:
	if root is None:
		return 0
	if root.val < L:
		return rangeSumBST1(root.right, L, R)
	if root.val > R:
		return rangeSumBST1(root.left, L, R)

	return root.val + rangeSumBST1(root.left, L, R) + rangeSumBST1(root.right, L, R)


if __name__ == '__main__':
	root = "10, 5, 15, 3, 7, null, 18"
	L = 7
	R = 15
	root = stringToTreeNode(root)
	result = rangeSumBST(root, L, R)
	print(result)
