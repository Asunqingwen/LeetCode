# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 16:45
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Two Sum Less Than K.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""
import sys
from typing import List


def twoSumLessThanK(A: List[int], K: int) -> int:
	A.sort()
	head, tail = 0, len(A) - 1
	res = sys.maxsize
	while head < tail:
		tmp = A[head] + A[tail]
		if tmp >= K:
			tail -= 1
			while head < tail and A[tail] == A[tail + 1]:
				tail -= 1
		elif tmp < K:
			if abs(tmp - K) < abs(res - K):
				res = tmp
			head += 1
			while head < tail and A[head] == A[head - 1]:
				head += 1
	if res == sys.maxsize:
		return -1
	else:
		return res


if __name__ == '__main__':
	A = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
	K = 200
	result = twoSumLessThanK(A, K)
	print(result)
