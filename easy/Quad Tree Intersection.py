# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 0003 14:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Quad Tree Intersection.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

For example, below are two quad trees A and B:

A:
+-------+-------+   T: true
|       |       |   F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight: T
bottomLeft: F
bottomRight: F

Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.

Note:

Both A and B represent grids of size N * N.
N is guaranteed to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
The logic OR operation is defined as this: "A or B" is true if A is true, or if B is true, or if both A and B are true.
"""


# Definition for a QuadTree node.
class Node:
	def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
		self.val = val
		self.isLeaf = isLeaf
		self.topLeft = topLeft
		self.topRight = topRight
		self.bottomLeft = bottomLeft
		self.bottomRight = bottomRight


def intersect(quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
	if quadTree1.isLeaf:
		if quadTree1.val:
			return quadTree1
		else:
			return quadTree2
	if quadTree2.isLeaf:
		if quadTree2.val:
			return quadTree2
		else:
			return quadTree1

	topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft)
	topRight = intersect(quadTree1.topRight, quadTree2.topRight)
	bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
	bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight)
	if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight and topLeft.val and topRight.val and bottomLeft.val and bottomRight.val:
		return Node(True, True, None, None, None, None)
	return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)


if __name__ == '__main__':
	input = 0
	intersect()
