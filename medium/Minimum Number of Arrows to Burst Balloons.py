# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 10:14
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum Number of Arrows to Burst Balloons.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
	if not points:
		return 0
	points.sort()
	res = 1
	pre = 0
	for curr in range(1, len(points)):
		if points[pre][0] <= points[curr][0] <= points[pre][-1]:
			if points[pre][-1] >= points[curr][-1]:
				pre = curr
			continue
		res += 1
		pre = curr
	return res


if __name__ == '__main__':
	points = [[-4, -3], [-8, -1], [-1, 9]]
	result = findMinArrowShots(points)
	print(result)
