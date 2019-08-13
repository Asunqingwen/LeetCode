# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 16:21
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Subarray Sum Equals K.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
import time
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
	sum_dict = {0: 1}
	sums = 0
	count = 0
	for num in nums:
		sums += num
		if sums - k in sum_dict:
			count += sum_dict[sums - k]
		sum_dict[sums] = sum_dict.get(sums, 0) + 1
	return count


if __name__ == '__main__':
	A = [1, 1, 1, 1, 1, 1, 1]
	K = 2
	start_time = time.time()
	result = subarraySum(A, K)
	end_time = time.time()
	print(result)
	print(end_time - start_time)
