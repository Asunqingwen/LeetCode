# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 0006 16:15
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Pascal's Triangle II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0
"""

from typing import List


def getRow(rowIndex: int) -> List[int]:
	nums = [[1]]
	for i in range(1, rowIndex + 1):
		num = [1] + [sum(nums[-1][j:j + 2]) for j in range(i)]
		nums.append(num)

	return nums[rowIndex]

def getRow1(rowIndex: int) -> List[int]:
	res = [1]
	if rowIndex != 0:
		res.append(1)
	for i in range(2,rowIndex + 1):
		res.insert(1, res[0] + res[1])
		for j in range(2, i):
			res[j] = res[j] + res[j + 1]
	return res

if __name__ == '__main__':
	m = 3

	result = getRow1(m)
	print(result)
