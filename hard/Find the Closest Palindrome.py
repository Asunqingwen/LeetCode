# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 10:11
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Find the Closest Palindrome.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""


def nearestPalindromic(n: str) -> str:
	size = len(n)
	if size == 1:
		return str(int(n) - 1)
	if n in ["10", "11"]:
		return "9"
	palindromic_list = []
	mid = size // 2
	if size % 2:
		left_str = n[:mid + 1]
	else:
		left_str = n[:mid]

	for i in range(-1, 2):
		left_part = str(int(left_str) - i)
		if left_part == '0':
			continue
		cat_str = left_part[:mid]
		cat_str = left_part + cat_str[::-1]

		if len(n) - len(cat_str) > 1:
			cat_str += cat_str[0]
		palindromic_list.append(cat_str)
	palindromic_list = [int(p) for p in palindromic_list if p != n]
	gap = abs(palindromic_list[0] - int(n))
	res = palindromic_list[0]
	for p in palindromic_list[1:]:
		g = abs(p - int(n))
		if g < gap:
			res, gap = p, g
		elif g == gap:
			if p < res:
				res = p

	return str(res)


if __name__ == '__main__':
	input = "88"
	result = nearestPalindromic(input)
	print(result)
