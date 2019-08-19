# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 15:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Climbing Stairs.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


def climbStairs(n: int) -> int:
	if n <= 1:
		return 1
	ways = 0
	n0 = 1
	n1 = 1
	for i in range(2, n+1):
		ways = n1 + n0
		n0, n1 = n1, ways
	return ways


if __name__ == '__main__':
	input = 3
	result = climbStairs(input)
	print(result)
