# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 15:16
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rectangle Area.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
"""


def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
	total_area = (C - A) * (D - B) + (G - E) * (H - F)
	if C < E or D < F or G < A or H < B:
		return total_area
	cov_area = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
	return total_area - cov_area


if __name__ == '__main__':
	A, B, C, D, E, F, G, H = -2,-2,2,2,3,3,4,4
	result = computeArea(A, B, C, D, E, F, G, H)
	print(result)
