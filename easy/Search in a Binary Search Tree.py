# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 14:20
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Search in a Binary Search Tree.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
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


def searchBST(root: TreeNode, val: int) -> TreeNode:
	stack_list = [root]
	while stack_list:
		node = stack_list.pop(0)
		if val < node.val and node.left:
			stack_list.append(node.left)
		elif val > node.val and node.right:
			stack_list.append(node.right)
		elif val == node.val:
			return node
		else:
			return None


if __name__ == '__main__':
	input1 = "8078,5196,8584,2401,5510,8450,8664,1343,4452,5356,7906,8118,8512,null,8821,220,1642,3158,5007,5288,5487,7711,null,null,8142,null,8527,8789,9584,105,769,1542,1857,2632,4380,4707,5188,null,null,null,null,6872,null,null,8290,null,null,null,null,9038,9905,null,null,621,958,1491,1564,1788,2321,2504,2942,3924,null,4500,null,null,null,6293,7117,8281,null,8943,9304,null,null,445,null,795,1285,1422,null,null,null,null,null,2202,null,2497,null,2929,3100,3715,4308,null,null,5709,6544,null,7561,8213,null,null,null,9245,null,null,null,null,null,1060,null,null,1446,2042,2296,null,null,2701,null,3057,null,3203,3753,4119,null,null,6016,null,6851,7500,null,null,null,9050,9253,null,null,null,null,null,2187,null,null,null,2901,3046,null,null,3227,null,3779,3956,null,5942,null,null,null,7232,7529,null,9153,null,null,null,null,2713,null,null,null,null,3558,null,null,null,null,5922,null,null,null,null,null,9126,9188,null,2855,3390,null,5758,null,null,null,null,null,null,null,null,3441,null,null,null,null"
	root = stringToTreeNode(input1)
	result = searchBST(root, 7906)
	result = treeNodeToString(result)
	print(result)
