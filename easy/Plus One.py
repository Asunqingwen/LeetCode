# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 0005 11:40
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Plus One.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
from typing import List


def plusOne(digits: List[int]) -> List[int]:
	plusOne = 1

	for i in range(len(digits) - 1, -1, -1):
		sum = digits[i] + plusOne
		div = sum // 10
		if not div:
			digits[i] = sum
			return digits
		else:
			digits[i] = sum % 10
			plusOne = div
	if not digits[i]:
		digits.insert(0, 1)
	return digits


def plusOne1(digits: List[int]) -> List[int]:
	size = len(digits)
	return [int(s) for s in str(sum([digit * 10 ** (size - index - 1) for index, digit in enumerate(digits)]) + 1)]


if __name__ == '__main__':
	nums = [1, 2, 3]
	result = plusOne1(nums)
	print(result)
