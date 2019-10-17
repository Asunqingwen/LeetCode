# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 0017 9:19
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximize Sum Of Array After K Negations.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
"""
from typing import List


def largestSumAfterKNegations(A: List[int], K: int) -> int:
	count = [0] * 201
	for a in A:
		count[a + 100] += 1
	for i in range(1, K + 1):
		j = 0
		while j < 201:
			if count[j] > 0:
				tmp_index = 200 - j
				count[tmp_index] += 1
				count[j] -= 1
				break
			j += 1
	res = 0
	for index, c in enumerate(count):
		while c > 0:
			res += (index - 100)
			c -= 1
	return res


if __name__ == '__main__':
	A = [2, -3, -1, 5, -4]
	K = 2
	result = largestSumAfterKNegations(A, K)
	print(result)
