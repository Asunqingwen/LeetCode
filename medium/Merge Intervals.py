# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 0027 10:47
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Merge Intervals.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
	if not intervals:
		return []
	intervals.sort(key=lambda x: x[0])
	queue = [intervals[0][1]]
	ans = intervals[0]
	res = []
	for i in range(1, len(intervals)):
		tmp = queue[0]
		if intervals[i][0] <= tmp:
			ans[1] = max(intervals[i][1], ans[1])
		else:
			res.append(ans)
			ans = intervals[i]
		queue.pop(0)
		queue.append(ans[1])
		queue.sort()
	res.append(ans)
	return res


def merge1(intervals: List[List[int]]) -> List[List[int]]:
	if not intervals:
		return []
	intervals.sort(key=lambda x: x[0])
	res = [intervals[0]]
	for interval in intervals[1:]:
		if interval[0] <= res[-1][1]:
			res[-1][1] = max(res[-1][1], interval[1])
		else:
			res.append(interval)
	return res


if __name__ == '__main__':
	input = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]
	result = merge(input)
	print(result)
