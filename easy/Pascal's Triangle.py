# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 0006 15:15
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Pascal's Triangle.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
	if not numRows:
		return []
	nums = [[1]]
	for i in range(1, numRows):
		num = [1] + [sum(nums[-1][j:j + 2]) for j in range(i)]
		nums.append(num)

	return nums


if __name__ == '__main__':
	m = 3

	result = generate(m)
	print(result)
