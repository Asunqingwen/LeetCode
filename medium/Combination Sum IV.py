# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 17:23
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Combination Sum IV.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""
from typing import List


# 回溯，超时，求具体解
def combinationSum4(nums: List[int], target: int) -> int:
	res = 0
	ans = []
	nums.sort()

	def helper(target):
		if target == 0:
			nonlocal res
			res += 1
			return
		for num in nums:
			if num > target:
				return
			ans.append(num)
			helper(target - num)
			ans.pop()

	helper(target)
	return res


# 动态规划，求解的个数
def combinationSum41(nums: List[int], target: int) -> int:
	dp = [0] * (target + 1)
	dp[0] = 1
	for i in range(1, target + 1):
		for num in nums:
			if i >= num:
				dp[i] += dp[i - num]
	return dp[target]


if __name__ == '__main__':
	nums = [1, 2, 3]
	target = 4
	result = combinationSum41(nums, target)
	print(result)
