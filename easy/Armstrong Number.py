# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 0022 17:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Armstrong Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

 

Example 1:

Input: 153
Output: true
Explanation:
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation:
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 

Note:

1 <= N <= 10^8
"""


def isArmstrong(N: int) -> bool:
	S = str(N)
	size = len(S)
	ans = 0
	for ss in S:
		ans += int(ss) ** size
	return ans == N


if __name__ == '__main__':
	N = 153
	result = isArmstrong(N)
	print(result)
