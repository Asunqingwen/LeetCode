# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0023 14:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Array Nesting.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

 

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
 

Note:

N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""
from typing import List


def arrayNesting(nums: List[int]) -> int:
	big_count = 0
	for num in nums:
		if num is 20000:
			continue
		count = 0
		while nums[num] is not 20000:
			temp = nums[num]
			nums[num] = 20000
			num = temp
			count += 1
		big_count = max(count, big_count)
	return big_count


if __name__ == '__main__':
	input = [5, 4, 0, 3, 1, 6, 2]
	output = arrayNesting(input)
	print(output)
