# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 0018 9:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Numbers With Same Consecutive Differences.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9
"""


# 超时
def numsSameConsecDiff(N, K):
	"""
	:type N: int
	:type K: int
	:rtype: List[int]
	"""
	if N == 1:
		return [i for i in range(10)]

	def helper(num):
		num_s = str(num)
		for i in range(1, len(num_s)):
			if abs(int(num_s[i]) - int(num_s[i - 1])) != K:
				return False
		return True

	start, end = 10 ** (N - 1), 10 ** N
	res = []
	for num in range(start, end):
		if helper(num):
			res.append(num)
	return res


def numsSameConsecDiff1(N, K):
	res = range(10)
	for _ in range(N - 1):
		ans = set()
		for x in res:
			for y in [x % 10 + K, x % 10 - K]:
				if x and 0 <= y <= 9:
					ans.add(x * 10 + y)
		res = ans
	return list(res)


if __name__ == '__main__':
	N = 3
	K = 7
	result = numsSameConsecDiff1(N, K)
	print(result)
