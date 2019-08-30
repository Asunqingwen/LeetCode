# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0023 11:32
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum Increment to Make Array Unique.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000
"""
from typing import List


def minIncrementForUnique(A: List[int]) -> int:
	if not A:
		return 0
	A = sorted(A)
	count = 0
	add_num = []
	h1 = 0
	h2 = h1 + 1
	while h2 < len(A):
		if A[h2] == A[h1]:
			add_num.append(A[h2])
			h2 += 1
		else:
			temp_list = [i for i in range(A[h1] + 1, A[h2])]
			if len(temp_list) == 0:
				h1 = h2
				h2 += 1
				continue
			elif len(temp_list) >= len(add_num):
				count += sum(temp_list[:len(add_num)]) - sum(add_num)
			else:
				count += sum(temp_list) - sum(add_num[:len(temp_list)])
			add_num = add_num[len(temp_list):]
			h1 = h2
			h2 += 1
	count += (2 * A[h2 - 1] + len(add_num) + 1) * len(add_num) // 2 - sum(add_num)
	return count


def minIncrementForUnique1(A: List[int]) -> int:
	if not A:
		return 0
	count = 0
	A = sorted(A)
	num = A[0]
	for i in range(1, len(A)):
		if A[i] <= num:
			count += num - A[i] + 1
			num += 1
		else:
			num = A[i]
	return count


if __name__ == '__main__':
	input = [3, 2, 1, 2, 1, 7]
	output = minIncrementForUnique1(input)
	print(output)
