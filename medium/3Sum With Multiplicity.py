# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 0029 13:45
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 3Sum With Multiplicity.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
 

Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""
from typing import List


def threeSumMulti(A: List[int], target: int) -> int:
	count = [0] * 101
	for a in A:
		count[a] += 1
	min, max = 0, 0
	for i in range(101):
		if count[i] != 0:
			min = i
			break
	for i in range(100, -1, -1):
		if count[i] != 0:
			max = i
			break
	res = 0
	for i in range(min, max + 1):
		head, tail = i, max
		while head <= tail:
			# if count[head] == 0:
			# 	head += 1
			# 	continue
			# elif count[tail] == 0:
			# 	tail -= 1
			# 	continue
			# else:
				a, b, c = i, head, tail
				if b + c < target - a:
					head += 1
				elif b + c > target - a:
					tail -= 1
				else:
					if a < b < c:
						res += count[i] * count[head] * count[tail]
					elif a == b < c:
						res += count[i] * (count[i] - 1) // 2 * count[tail]
					elif a < b == c:
						res += count[head] * (count[head] - 1) // 2 * count[i]
					else:
						res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
					head += 1
					tail -= 1
					res %= 1000000007
	return res


if __name__ == '__main__':
	A = [1,1,2,2,2,2]
	target = 5
	result = threeSumMulti(A, target)
	print(result)
