# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 0027 9:32
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Meeting Rooms.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
	intervals.sort(key=lambda x: x[0])
	for i in range(1, len(intervals)):
		if intervals[i][0] < intervals[i - 1][1]:
			return False
	return True


if __name__ == '__main__':
	input = [[0, 30], [5, 10], [15, 20]]
	result = canAttendMeetings(input)
	print(result)
