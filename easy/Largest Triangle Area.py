# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 0009 9:25
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Largest Triangle Area.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""
from typing import List


def largestTriangleArea(points: List[List[int]]) -> float:
	max_area = 0.0
	n = len(points)
	for i in range(n-2):
		for j in range(i+1, n-1):
			for k in range(j+1, n):
				x1, y1 = points[i][0], points[i][1]
				x2, y2 = points[j][0], points[j][1]
				x3, y3 = points[k][0], points[k][1]
				#三角形面积坐标公式
				tmp_area = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2
				max_area = max(tmp_area, max_area)
	return max_area


if __name__ == '__main__':
	points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
	result = largestTriangleArea(points)
	print(result)
