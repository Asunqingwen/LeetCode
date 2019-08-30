# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 17:45
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Largest Unique Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation:
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

Note:

1 <= A.length <= 2000
0 <= A[i] <= 1000
相关企业：亚马逊
标签：数组，哈希表
"""
from typing import List


def largestUniqueNumber(A: List[int]) -> int:
	count = {}
	for num in A:
		count[num] = count.get(num, 0) + 1

	max_value = -1
	for key, value in count.items():
		if value == 1:
			max_value = max(max_value, key)
	return max_value


if __name__ == '__main__':
	input = [5, 7, 3, 9, 4, 9, 8, 3, 1]
	result = largestUniqueNumber(input)
	print(result)
