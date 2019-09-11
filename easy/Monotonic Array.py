# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 0011 11:13
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Monotonic Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""
from typing import List


def isMonotonic(A: List[int]) -> bool:
	desc = False
	asc = False
	for i in range(len(A) - 1):
		right = A[i + 1]
		desc = desc or (A[i] > right)
		asc = asc or (A[i] < right)
		if desc and asc:
			return False
	return True


if __name__ == '__main__':
	input = []
	result = isMonotonic(input)
	print(result)
