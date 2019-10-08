# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 15:23
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Set Mismatch.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
	finder, sum, n = 0, 0, len(nums)
	for num in nums:
		if nums[abs(num) - 1] > 0:
			nums[abs(num) - 1] = - nums[abs(num) - 1]
		else:
			finder = abs(num)
		sum += abs(num)
	return [finder, finder - (sum - (n * n + n) // 2)]


if __name__ == '__main__':
	nums = [3, 2, 3]
	result = findErrorNums(nums)
	print(result)
