# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 0007 17:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Largest Number At Least Twice of Others.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""
from typing import List


def dominantIndex(nums: List[int]) -> int:
	max_v = max(nums)
	index = nums.index(max_v)
	for num in nums[:index]:
		if max_v < (num << 1):
			return -1
	for num in nums[index + 1:]:
		if max_v < (num << 1):
			return -1
	return index


if __name__ == '__main__':
	nums = [3, 6, 1, 0]
	result = dominantIndex(nums)
	print(result)
