# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 0014 16:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Missing Ranges.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
from typing import List


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
	if not nums:
		if lower == upper:
			return [str(lower)]
		return [str(lower) + '->' + str(upper)]
	res = []
	ans = []
	i = 0
	while i < len(nums):
		j = i
		while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
			i += 1
		if i == j:
			ans.append([nums[i]])
		else:
			ans.append([nums[j], nums[i]])
		i += 1
	if ans[0][0] == lower + 1:
		res.append(str(lower))
	elif ans[0][0] > lower + 1:
		res.append(str(lower) + '->' + str(ans[0][0] - 1))
	for i in range(1, len(ans)):
		if ans[i][0] - ans[i - 1][-1] == 2:
			res.append(str(ans[i][0] - 1))
		elif ans[i][0] > ans[i - 1][-1] + 2:
			res.append(str(ans[i - 1][-1] + 1) + '->' + str(ans[i][0] - 1))
	if ans[-1][-1] == upper - 1:
		res.append(str(upper))
	elif ans[-1][-1] < upper - 1:
		res.append(str(ans[-1][-1] + 1) + '->' + str(upper))
	return res


if __name__ == '__main__':
	nums = [1, 1, 1, 1, 1]
	lower = 1
	upper = 1
	result = findMissingRanges(nums, lower, upper)
	print(result)
