# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 0018 9:07
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Bulb Switcher II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
 

Example 1:

Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]
"""


def flipLights(n: int, m: int) -> int:
	if n == 0 or m == 0:
		return 1
	if n == 1:
		return 2
	if n == 2:
		return 3 if m == 1 else 4
	if m == 1:
		return 4
	if m == 2:
		return 7
	return 8


if __name__ == '__main__':
	n = 2
	m = 1
	result = flipLights(n, m)
	print(result)
