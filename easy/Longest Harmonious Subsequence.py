# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 0024 14:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Longest Harmonious Subsequence.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 

Note: The length of the input array will not exceed 20,000.
"""
from typing import List


def findLHS(nums: List[int]) -> int:
	count = {}
	for num in nums:
		count[num] = count.get(num, 0) + 1
	res = 0
	for item in count.keys():
		if item + 1 in count:
			res = max(res, count[item] + count[item + 1])
	return res


if __name__ == '__main__':
	input = [1, 3, 2, 2, 5, 2, 3, 7]
	result = findLHS(input)
	print(result)
