# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 0005 16:34
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Merge Sorted Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	"""
	Do not return anything, modify nums1 in-place instead.
	"""
	if nums1[m - 1] <= nums2[0]:
		nums1.extend(nums2)
	if nums1[0] >= nums2[n - 1]:
		nums1 = nums2.extend(nums1)

	k1 = 0
	k2 = 0
	nums3 = list()
	while k1 < m and k2 < n:
		if nums1[k1] <= nums2[k2]:
			nums3.append(nums1[k1])
			k1 += 1
		else:
			nums3.append(nums2[k2])
			k2 += 1
	if k1 < m:
		nums3.extend(nums1[k1:])
	if k2 < n:
		nums3.extend(nums2[k2:])
	nums1 = nums3
	return nums1


def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	nums1.extend(nums2)
	nums1.sort()
	return nums1


def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	k1 = m - 1
	k2 = n - 1

	for i in range(m + n - 1, -1, -1):
		if k1 == -1:
			nums1[i] = nums2[k2]
			k2 -= 1
		elif k2 == -1:
			break
		elif nums1[k1] < nums2[k2]:
			nums1[i] = nums2[k2]
			k2 -= 1
		else:
			nums1[i] = nums1[k1]
			k1 -= 1

def merge3(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	k1 = m - 1
	k2 = n - 1

	for i in range(m + n - 1, -1, -1):
		if k2 == -1:
			break
		elif nums1[k1] < nums2[k2]:
			nums1[i] = nums2[k2]
			k2 -= 1
		else:
			nums1[i] = nums1[k1]
			k1 -= 1
	nums1[:k2 + 1] = nums2[:k2 + 1]


if __name__ == '__main__':
	nums1 = [1, 2, 3, 0, 0, 0]
	m = 3
	nums2 = [2, 5, 6]
	n = 3

	result = merge3(nums1, m, nums2, n)
	print(nums1)
