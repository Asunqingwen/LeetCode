# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 14:34
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Find the Duplicate Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
from typing import List


#类似于找到链表中的环
def findDuplicate(nums: List[int]) -> int:
	fast, slow = 0, 0
	while True:
		fast, slow = nums[nums[fast]], nums[slow]
		if fast == slow:
			break
	finder = 0
	while True:
		finder, slow = nums[finder], nums[slow]
		if finder == slow:
			break
	return finder


if __name__ == '__main__':
	input = [3, 1, 3, 4, 2]
	result = findDuplicate(input)
	print(result)
