# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 0009 9:48
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Largest Perimeter Triangle.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8
 

Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""
from typing import List


def largestPerimeter(A: List[int]) -> int:
	A.sort(reverse=True)
	for i in range(2, len(A)):
		if A[i - 1] + A[i] > A[i - 2]:
			return A[i] + A[i - 1] + A[i - 2]
	return 0


if __name__ == '__main__':
	A = [1, 2, 1]
	result = largestPerimeter(A)
	print(result)
