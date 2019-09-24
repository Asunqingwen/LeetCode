# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 0024 17:23
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Beautiful Arrangement II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
"""
from typing import List


# 超时
def constructArray(n: int, k: int) -> List[int]:
	res = []

	def helper(flag, n, count):
		if count == n + 1:
			tmp = [abs(res[i] - res[i + 1]) for i in range(len(res) - 1)]
			if len(set(tmp)) == k:
				return True
			else:
				return False
		for i in range(1, n + 1):
			if flag[i]:
				continue
			res.append(i)
			flag[i] = 1
			if helper(flag, n, count + 1):
				return True
			res.pop()
			flag[i] = 0

	flag = [0] * (n + 1)
	helper(flag, n, 1)
	return res


def constructArray1(n: int, k: int) -> List[int]:
	res = list(range(1, n + 1))
	for i in range(1, k):
		res[i:] = res[:i - 1:-1]
	return res


if __name__ == '__main__':
	n = 3
	k = 1
	result = constructArray1(n, k)
	print(result)
