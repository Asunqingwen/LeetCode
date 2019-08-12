# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 0005 9:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: solve.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
from typing import List


def removeElement(nums: List[int], val: int) -> int:
	if not nums:
		return 0
	k=0
	for i in range(len(nums)):
		if nums[i] != val:
			nums[k] = nums[i]
			k += 1
	return k



if __name__ == '__main__':
	nums = [3,2,2,3]
	result = removeElement(nums, 3)
	print(result)
