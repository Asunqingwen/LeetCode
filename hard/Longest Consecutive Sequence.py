# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 0012 9:12
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Longest Consecutive Sequence.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
	res = 0
	nums = set(nums)

	for num in nums:
		if num - 1 not in nums:
			curr = num
			ans = 1
			while curr + 1 in nums:
				curr += 1
				ans += 1
			res = max(res, ans)
	return res


if __name__ == '__main__':
	nums = [100, 4, 200, 1, 3, 2]
	result = longestConsecutive(nums)
	print(result)
