# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 9:26
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Distance to a Character.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
from typing import List


def shortestToChar(S: str, C: str) -> List[int]:
	res = []
	size = len(S)
	for i in range(size):
		left, right = i, i
		while left >= 0 and S[left] != C:
			left -= 1
		left = size + 1 if left == -1 else i - left

		while right < size and S[right] != C:
			right += 1
		right = size + 1 if right == size else right - i
		res.append(min(left, right))
	return res


if __name__ == '__main__':
	S = ""
	C = ''
	result = shortestToChar(S, C)
	print(result)
