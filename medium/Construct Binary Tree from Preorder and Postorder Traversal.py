# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0023 16:00
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Construct Binary Tree from Preorder and Postorder Traversal.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
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


def maxDepth(root: TreeNode) -> int:
	def getDepth(root: TreeNode) -> int:
		if not root:
			return 0
		res = max(getDepth(root.left), getDepth(root.right)) + 1
		return res

	return getDepth(root)


def constructFromPrePost(pre: List[int], post: List[int]) -> TreeNode:
	def getTree(pre, post):
		if pre:
			root = TreeNode(pre[0])
			if pre[1:]:
				if pre[1] == post[1]:
					root.left = getTree(pre[1:], post[1:])
				else:
					left_index = pre.index(post[1])
					right_index = post.index(pre[1])
					root.left = getTree(pre[1:left_index], post[right_index:])
					root.right = getTree(pre[left_index:], post[1:right_index])
			return root
	return getTree(pre, post[::-1])


if __name__ == '__main__':
	pre = [1, 2, 4, 5, 3, 6, 7]
	post = [4, 5, 2, 6, 7, 3, 1]
	output = constructFromPrePost(pre, post)
	print(treeNodeToString(output))
