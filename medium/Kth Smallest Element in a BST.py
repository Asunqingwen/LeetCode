# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 0014 10:49
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Kth Smallest Element in a BST.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine
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


def kthSmallest(root: TreeNode, k: int) -> int:
	count = 0
	ans = []
	while root or ans:
		if root:
			ans.append(root)
			root = root.left
		else:
			curr = ans.pop()
			count += 1
			if count == k:
				return curr.val
			root = curr.right




if __name__ == '__main__':
	input = "3,1,4,null,2"
	root = stringToTreeNode(input)
	result = kthSmallest(root,1)
	print(result)
