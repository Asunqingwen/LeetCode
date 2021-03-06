# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 9:35
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Non-overlapping Intervals.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
	intervals.sort()
	res = 0
	i = 0
	j = i + 1
	while j < len(intervals):
		while j < len(intervals) and intervals[i][-1] > intervals[j][0]:
			if intervals[i][0] < intervals[j][0]:
				if intervals[i][-1] > intervals[j][-1]:
					i = j
			res += 1
			j += 1
		i = j
		j = i + 1
	return res


if __name__ == '__main__':
	intervals = [ [1,2], [2,3] ]

	result = eraseOverlapIntervals(intervals)
	print(result)
