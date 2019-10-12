# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 0011 15:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Path With Maximum Minimum Value.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

 

Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation:
The path with the maximum score is highlighted in yellow.
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
 

Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9
"""
import heapq as hq
from typing import List


def maximumMinimumPath(A: List[List[int]]) -> int:
	row, col = len(A), len(A[0])
	# 坐标值必须放在最前面，因为heapq排序默认是以存储对象的第一个值进行排序的,然后再对第二个值排序，以此类推
	ans = [(-A[0][0], 0, 0)]
	A[0][0] = -1
	hq.heapify(ans)
	while ans:
		score, i, j = hq.heappop(ans)
		if (i, j) == (row - 1, col - 1):
			return -score
		for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			new_i = i + di
			new_j = j + dj
			if 0 <= new_i < row and 0 <= new_j < col:
				if A[new_i][new_j] != -1:
					hq.heappush(ans, (max(score, -A[new_i][new_j]), new_i, new_j))
					A[new_i][new_j] = -1


if __name__ == '__main__':
	A = [[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]
	result = maximumMinimumPath(A)
	print(result)
