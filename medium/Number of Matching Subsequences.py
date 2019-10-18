# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 0018 15:47
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Number of Matching Subsequences.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
from typing import List


def numMatchingSubseq(S: str, words: List[str]) -> int:
	def helper(word):
		index = 0
		for i in range(len(word)):
			res = S.find(word[i], index)
			if -1 == res:
				return False
			else:
				index = res + 1
		return True

	res = 0
	for word in words:
		if helper(word):
			res += 1
	return res


if __name__ == '__main__':
	S = "qlhxagxdqh"
	words = ["qlhxagxdq", "qlhxagxdq", "lhyiftwtut", "yfzwraahab"]
	result = numMatchingSubseq(S, words)
	print(result)
