# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 0008 13:52
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Random Point in Non-overlapping Rectangles.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
Example 1:

Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]
Example 2:

Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
from typing import List

import numpy as np
import numpy.random as npr
from random import randint


class Solution:

	def __init__(self, rects: List[List[int]]):
		self.rects = rects
		self.k = len(rects)
		self.sum_area = sum([(rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) for rect in rects])
		self.probs = []
		for rect in rects:
			self.probs.append((rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) / self.sum_area)
		self.Prob, self.Alias = self.alias_setup(self.k, self.probs)

	def alias_setup(self, k, probs):
		Prob = np.zeros(k)
		Alias = np.zeros(k, dtype=np.int)
		smaller, larger = [], []
		for kk, prob in enumerate(probs):
			Prob[kk] = k * prob
			if Prob[kk] < 1.0:
				smaller.append(kk)
			else:
				larger.append(kk)

		# 通过拼凑将各个类别凑为1
		while smaller and larger:
			small, large = smaller.pop(), larger.pop()

			Alias[small] = large
			Prob[large] = Prob[large] - (1.0 - Prob[small])
			if Prob[large] < 1.0:
				smaller.append(large)
			else:
				larger.append(large)
		return Prob, Alias

	def pick(self) -> List[int]:
		# 随机取一列
		kk = int(np.floor(npr.rand() * self.k))
		if npr.rand() < self.Prob[kk]:
			rect = self.rects[kk]
		else:
			rect = self.rects[self.Alias[kk]]
		return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
if __name__ == '__main__':
	rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]
	obj = Solution(rects)
	print(obj.pick())
	print(obj.pick())
	print(obj.pick())
	print(obj.pick())
	print(obj.pick())
	print(obj.pick())
	print(obj.pick())
	print(obj.pick())
	print(obj.pick())
