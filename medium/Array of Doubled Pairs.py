# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 10:42
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Array of Doubled Pairs.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

 

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false
 

Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000
"""
from typing import List


def canReorderDoubled(A: List[int]) -> bool:
	ne_list, po_list = [], []
	for a in A:
		if a < 0:
			ne_list.append(abs(a))
		elif a > 0:
			po_list.append(a)
	if len(ne_list) % 2 != 0 or len(po_list) % 2 != 0:
		return False

	def helper(data):
		data.sort()
		data_dict = {}
		for n in data:
			data_dict[n] = data_dict.get(n, 0) + 1
		for n in data:
			if data_dict[n] != 0:
				if n*2 not in data_dict or data_dict[n * 2] == 0:
					return False
				data_dict[n] -= 1
				data_dict[n * 2] -= 1
		return True

	return helper(ne_list) and helper(po_list)


if __name__ == '__main__':
	input = [0,3]
	result = canReorderDoubled(input)
	print(result)
