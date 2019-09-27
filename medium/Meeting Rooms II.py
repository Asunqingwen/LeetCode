# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 0027 9:47
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Meeting Rooms II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
	if not intervals:
		return 0
	intervals.sort(key=lambda x: x[0])
	ans = [intervals[0][1]]
	count = 1
	for i in range(1, len(intervals)):
		tmp = ans[0]
		if intervals[i][0] >= tmp:
			ans.pop(0)
		else:
			count += 1
		ans.append(intervals[i][1])
		ans.sort()
	return count


if __name__ == '__main__':
	input = [[1,8],[6,20],[9,16],[13,17]]
	result = minMeetingRooms(input)
	print(result)
