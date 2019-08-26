# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 10:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: DI String Match.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]
 

Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".
"""
from typing import List


def diStringMatch(S: str) -> List[int]:
	D_index = []
	I_index = []
	for index, s in enumerate(S):
		if s is 'D':
			D_index.append(index)
		else:
			I_index.append(index)
	nums = [i for i in range(len(S) + 1)]
	D_nums = nums[len(nums):len(nums) - len(D_index) - 1:-1]
	I_nums = nums[:len(I_index)]
	res_list = [0] * len(nums)
	res_list[len(S)] = nums[len(I_index)]
	for index, i in enumerate(D_index):
		res_list[i] = D_nums[index]
	for index, i in enumerate(I_index):
		res_list[i] = I_nums[index]
	return res_list


def diStringMatch1(S: str) -> List[int]:
	head = 0
	tail = len(S)
	res_list = []
	for s in S:
		if s is 'D':
			res_list.append(tail)
			tail -= 1
		else:
			res_list.append(head)
			head += 1
	res_list.append(head)
	return res_list


if __name__ == '__main__':
	input = "D"
	result = diStringMatch1(input)
	print(result)
