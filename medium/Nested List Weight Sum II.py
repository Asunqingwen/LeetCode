# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 17:21
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Nested List Weight Sum II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.

企业：领英
标签：深度优先搜索
"""
from typing import List

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
	def __init__(self, value=None):
		"""
		If value is not specified, initializes an empty list.
		Otherwise initializes a single integer equal to value.
		"""

	def isInteger(self):
		"""
		@return True if this NestedInteger holds a single integer, rather than a nested list.
		:rtype bool
		"""

	def add(self, elem):
		"""
		Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
		:rtype void
		"""

	def setInteger(self, value):
		"""
		Set this NestedInteger to hold a single integer equal to value.
		:rtype void
		"""

	def getInteger(self):
		"""
		@return the single integer that this NestedInteger holds, if it holds a single integer
		Return None if this NestedInteger holds a nested list
		:rtype int
		"""

	def getList(self):
		"""
		@return the nested list that this NestedInteger holds, if it holds a nested list
		Return None if this NestedInteger holds a single integer
		:rtype List[NestedInteger]
		"""


def depthSumInverse(nestedList: List[NestedInteger]) -> int:
	res = 0
	depth_weight = []

	def getDepth(nl, depth, depth_weight):
		if depth >= len(depth_weight):
			depth_weight.append(0)
		if nl.isInteger():
			depth_weight[depth] += nl.getInteger()
		else:
			for n in nl.getList():
				getDepth(n, depth + 1, depth_weight)

	for nest in nestedList:
		getDepth(nest, 0, depth_weight)

	for weight in range(len(depth_weight) - 1, -1, -1):
		res += depth_weight[weight] * (len(depth_weight) - weight)
	return res


if __name__ == '__main__':
	input = list(NestedInteger([[1, 1], 2, [1, 1]]))
	result = depthSumInverse(input)
	print(result)
