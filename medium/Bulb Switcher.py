# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 15:18
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Bulb Switcher.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
"""

from math import sqrt, floor


# 超时
def bulbSwitch(n: int) -> int:
	ans = [0] * n
	if n <= 1:
		return n
	for i in range(n):
		for j in range(i, n, i + 1):
			ans[j] ^= 1
	return len([a for a in ans if a])


def bulbSwitch1(n: int) -> int:
	return floor(sqrt(n))


if __name__ == '__main__':
	input = 3
	result = bulbSwitch(input)
	print(result)
