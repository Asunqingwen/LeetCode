# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 10:59
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Happy Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


def isHappy(n: int) -> bool:
	ans = {1}
	while n not in ans:
		ans.add(n)
		n = sum(int(i) ** 2 for i in str(n))
	return n == 1


if __name__ == '__main__':
	n = 19
	result = isHappy(n)
	print(result)
