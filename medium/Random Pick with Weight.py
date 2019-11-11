# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 0008 14:26
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Random Pick with Weight.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
from typing import List

import numpy as np
import numpy.random as npr


class Solution:

	def __init__(self, w: List[int]):
		# 类别个数
		self.k = len(w)
		# 每个数占总和的权重
		self.probs = []
		self.sum = sum(w)
		for ww in w:
			self.probs.append(ww / self.sum)
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

		# 通过拼凑，将各个类别都凑为1
		while len(smaller) > 0 and len(larger) > 0:
			small = smaller.pop()
			large = larger.pop()

			Alias[small] = large
			Prob[large] = Prob[large] - (1.0 - Prob[small])  # 将大的分到小的上

			if Prob[large] < 1.0:
				smaller.append(large)
			else:
				larger.append(large)
		return Prob, Alias

	def pickIndex(self) -> int:
		# 随机取一列
		kk = int(np.floor(npr.rand() * self.k))
		if npr.rand() < self.Prob[kk]:
			return kk
		else:
			return self.Alias[kk]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
if __name__ == '__main__':
	w = [1, 3]
	obj = Solution(w)
	print(obj.pickIndex())
	print(obj.pickIndex())
	print(obj.pickIndex())
	print(obj.pickIndex())
	print(obj.pickIndex())
	print(obj.pickIndex())
