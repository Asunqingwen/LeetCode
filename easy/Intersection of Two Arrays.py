# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 17:57
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Intersection of Two Arrays.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Note:

Each element in the result must be unique.
The result can be in any order.

企业：阿里巴巴 优步 苹果 当当 百度
标签：排序 哈希表 双指针 二分查找
"""
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
	count = {}
	for num in nums1:
		count[num] = 0
	res = set()
	for num in nums2:
		if num in count:
			res.add(num)
	return list(res)

def intersection1(nums1: List[int], nums2: List[int]) -> List[int]:
	nums1 = set(nums1)
	nums2 = set(nums2)
	res = []
	for num in nums1:
		if num in nums2:
			res.append(num)
	return res


if __name__ == '__main__':
	nums1 = [4, 9, 5]
	nums2 = [9, 4, 9, 8, 4]
	result = intersection(nums1, nums2)
	print(result)
