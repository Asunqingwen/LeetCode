# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 0004 10:21
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Kth Largest Element in an Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
	heapq.heapify(nums)
	while len(nums) > k:
		heapq.heappop(nums)
	return nums[0]


if __name__ == '__main__':
	input = [3,2,1,5,6,4]
	k = 2
	result = findKthLargest(input, k)
	print(result)
