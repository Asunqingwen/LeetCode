# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 0012 17:05
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Longest Word in Dictionary.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""
from typing import List


def longestWord(words: List[str]) -> str:
	word_set = set(words)
	res = []
	max_len = 0
	for word in words:
		i = 1
		while i <= len(word):
			if word[:i] not in word_set:
				break
			i += 1
		if i == len(word) + 1:
			if max_len < len(word):
				res.clear()
				res.append(word)
				max_len = len(word)
			elif max_len == len(word):
				res.append(word)
	res.sort()
	return res[0]


def longestWord1(words: List[str]) -> str:
	dict = [[] for _ in range(31)]
	for word in words:
		dict[len(word)].append(word)

	longestword = set(dict[1])
	for i in range(2, 31):
		tmp = {w for w in dict[i] if w[:-1] in longestword}
		if not tmp:
			break
		longestword = tmp

	return sorted(list(longestword))[0]




if __name__ == '__main__':
	words = ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
	result = longestWord1(words)
	print(result)
