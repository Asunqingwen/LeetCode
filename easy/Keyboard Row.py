# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 0012 11:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Keyboard Row.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
from typing import List


def findWords(words: List[str]) -> List[str]:
	if not words or not words[0]:
		return words
	row1 = {'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o', 'p': 'p'}
	row2 = {'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l'}
	row3 = {'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm'}

	def helper(word, row):
		count = 0
		while count < len(word):
			if word[count] not in row:
				break
			count += 1
		return count == len(word)

	res = []
	for word in words:
		tmp = word.lower()
		flag = False
		if tmp[0] in row1:
			flag = helper(tmp, row1)
		elif tmp[0] in row2:
			flag = helper(tmp, row2)
		elif tmp[0] in row3:
			flag = helper(tmp, row3)
		if flag:
			res.append(word)
	return res


def findWords1(words):
	set1 = set('qwertyuiop')
	set2 = set('asdfghjkl')
	set3 = set('zxcvbnm')
	res = []
	for i in words:
		x = i.lower()
		setx = set(x)
		if setx <= set1 or setx <= set2 or setx <= set3:
			res.append(i)
	return res


if __name__ == '__main__':
	words = ["Hello", "Alaska", "Dad", "Peace"]
	result = findWords1(words)
	print(result)
