# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 14:51
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Word Distance.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
from typing import List


def shortestDistance(words: List[str], word1: str, word2: str) -> int:
	i1, i2 = -1, -1
	min_dis = len(words)
	for i in range(len(words)):
		if words[i] == word1:
			i1 = i
		elif words[i] == word2:
			i2 = i
		if i1 != -1 and i2 != -1:
			min_dis = min(min_dis, abs(i1 - i2))
	return min_dis


if __name__ == '__main__':
	words = ["practice", "makes", "perfect", "coding", "makes"]
	word1 = "makes"
	word2 = "coding"
	result = shortestDistance(words, word1, word2)
	print(result)
