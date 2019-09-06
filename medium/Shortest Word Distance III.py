# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 15:59
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Word Distance III.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
"""
import sys
from typing import List


def shortestWordDistance(words: List[str], word1: str, word2: str) -> int:
	i1, i2 = -1, -1
	min_dis = sys.maxsize
	if word1 == word2:
		for index, word in enumerate(words):
			if word == word1:
				i2, i1 = i1, index
			if i1 != -1 and i2 != -1:
				min_dis = min(min_dis, i1 - i2)
	else:
		for index, word in enumerate(words):
			if word == word1:
				i1 = index
			elif word == word2:
				i2 = index
			if i1 != -1 and i2 != -1:
				min_dis = min(min_dis, abs(i1 - i2))
	return min_dis


if __name__ == '__main__':
	words = ["a", "c", "a", "a"]
	word1 = "a"
	word2 = "a"
	result = shortestWordDistance(words, word1, word2)
	print(result)
