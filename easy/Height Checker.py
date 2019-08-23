# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0023 9:37
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Height Checker.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

 

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right positions.
 

Note:

1 <= heights.length <= 100
1 <= heights[i] <= 100
"""
from typing import List


def heightChecker(heights: List[int]) -> int:
	count_list = [0] * 101
	for height in heights:
		count_list[height] += 1
	i = 0
	count = 0
	for j in range(101):
		while count_list[j] > 0:
			if heights[i] != j:
				count += 1
			i += 1
			count_list[j] -= 1

	return count


if __name__ == '__main__':
	input = [2, 6, 8, 6, 5, 2, 4, 3, 7, 3, 7, 5, 6, 6, 2, 4, 4, 6, 8, 4, 5]
	output = heightChecker(input)
	print(output)
