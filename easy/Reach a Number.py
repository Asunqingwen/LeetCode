# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 0011 9:18
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reach a Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""


def reachNumber(target: int) -> int:
	target = abs(target)
	sum = 0
	move = 1
	while True:
		sum += move
		if sum >= target and (sum - target) % 2 == 0:
			return move
		move += 1


if __name__ == '__main__':
	target = 2
	result = reachNumber(target)
	print(result)
