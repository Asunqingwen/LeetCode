# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 13:44
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Flood Fill.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
	if newColor == image[sr][sc]:
		return image
	row, col = len(image), len(image[0])
	queue_list = [[sr, sc]]
	init_color = image[sr][sc]
	image[sr][sc] = newColor
	while queue_list:
		x, y = queue_list.pop(0)
		l, r, u, d = y - 1, y + 1, x - 1, x + 1
		if l >= 0 and image[x][l] == init_color:
			image[x][l] = newColor
			queue_list.append([x, l])
		if r < col and image[x][r] == init_color:
			image[x][r] = newColor
			queue_list.append([x, r])
		if u >= 0 and image[u][y] == init_color:
			image[u][y] = newColor
			queue_list.append([u, y])
		if d < row and image[d][y] == init_color:
			image[d][y] = newColor
			queue_list.append([d, y])

	return image


if __name__ == '__main__':
	image = [[0, 0, 0], [0, 1, 1]]
	sr = 1
	sc = 1
	newColor = 1
	result = floodFill(image, sr, sc, newColor)
	print(result)
