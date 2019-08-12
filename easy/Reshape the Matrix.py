# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 0009 11:42
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reshape the Matrix.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""
from typing import List


def matrixReshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
	one_nums = []
	for num in nums:
		one_nums.extend(num)

	if len(one_nums) < r * c:
		return nums

	return_nums = []
	for i in range(r):
		temp_nums = one_nums[i*c:(i+1)*c]
		return_nums.append(temp_nums)
	return return_nums

if __name__ == '__main__':
	nums = [[1,2,3,4]]
	r = 2
	c = 2
	result = matrixReshape(nums,r,c)
	print(result)
