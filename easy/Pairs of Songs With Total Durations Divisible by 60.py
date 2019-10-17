# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 0017 14:50
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Pairs of Songs With Total Durations Divisible by 60.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""
from typing import List


def numPairsDivisibleBy60(time: List[int]) -> int:
	res = 0
	mod = [0] * 60
	for t in time:
		index = t % 60
		mod[index] += 1
	for i, n in enumerate(mod):
		if i == 0 or i == 30:
			res += mod[i] * (mod[i] - 1) // 2
		else:
			res += mod[i] * mod[60 - i]
			mod[60 - i] = 0
	return res


if __name__ == '__main__':
	time = [418, 204, 77, 278, 239, 457, 284, 263, 372, 279, 476, 416, 360, 18]
	result = numPairsDivisibleBy60(time)
	print(result)
