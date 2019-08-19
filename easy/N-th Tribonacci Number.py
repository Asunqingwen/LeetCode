# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 16:00
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: N-th Tribonacci Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


def tribonacci(n: int) -> int:
	if n == 0:
		return 0
	elif n < 3:
		return 1
	t0 = 0
	t1 = 1
	t2 = 1
	tn = 0
	for i in range(3, n + 1):
		tn = t0 + t1 + t2
		t0, t1, t2 = t1, t2, tn
	return tn


if __name__ == '__main__':
	n = 25
	result = tribonacci(n)
	print(result)
