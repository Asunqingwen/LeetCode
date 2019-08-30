# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 16:57
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Nested List Weight Sum.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

企业：领英
标签：深度优先搜索
"""
from typing import List


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


def depthSum(nestedList: List[NestedInteger]) -> int:
	queue_list = []
	sum_list = 0
	for nest in nestedList:
		queue_list.append([nest, 1])
	while queue_list:
		curr = queue_list.pop(0)
		if curr[0].isInteger():
			sum_list += curr[0].getInteger() * curr[1]
		else:
			for c in curr[0].getList():
				queue_list.append([c, curr[1] + 1])
	return sum_list


if __name__ == '__main__':
	input = list(NestedInteger([[1, 1], 2, [1, 1]]))
	result = depthSum(input)
	print(result)
