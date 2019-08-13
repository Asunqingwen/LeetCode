# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 15:13
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Subarray Sums Divisible by K.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""
import time
from typing import List


def subarraysDivByK(A: List[int], K: int) -> int:
	P = [0]
	for index, num in enumerate(A):
		P.append(P[index] + num)
	mod_dict = {}
	for p in P:
		mod = p % K
		if mod in mod_dict:
			mod_dict[mod] += 1
		else:
			mod_dict[mod] = 1
	count = 0
	for mod in mod_dict.values():
		count = count + mod * (mod - 1) // 2
	return count


def subarraysDivByK1(A: List[int], K: int) -> int:
	s = 0
	cnt = 0
	remain = [1] + [0] * (K - 1)
	for num in A:
		s += num
		if K != 0:
			s %= K
		cnt += remain[s]
		remain[s] += 1
	return cnt


if __name__ == '__main__':
	A = [1, 1, 1]
	K = 2
	start_time = time.time()
	result = subarraysDivByK(A, K)
	end_time = time.time()
	print(result)
	print(end_time - start_time)
