# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 14:46
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Word Distance II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
import sys
from typing import List


class WordDistance:

	def __init__(self, words: List[str]):
		self.index_dict = {}
		for index, word in enumerate(words):
			if word in self.index_dict:
				self.index_dict[word].append(index)
			else:
				self.index_dict[word] = [index]

	def shortest(self, word1: str, word2: str) -> int:
		l1, l2 = self.index_dict[word1], self.index_dict[word2]
		min_dis = sys.maxsize
		i1, i2 = 0, 0
		while i1 < len(l1) and i2 < len(l2):
			if l1[i1] < l2[i2]:
				min_dis = min(min_dis, l2[i1] - l1[i1])
				i1 += 1
			else:
				min_dis = min(min_dis, l1[i1] - l2[i2])
				i2 += 1
		return min_dis


if __name__ == '__main__':
	words = ["practice", "makes", "perfect", "coding", "makes"]
	word1 = "coding"
	word2 = "practice"
	res = WordDistance(words)
	result = res.shortest(word1, word2)
	print(result)
