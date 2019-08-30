# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 17:16
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Spiral Matrix II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
相关企业：腾讯 Facebook 字节跳动 今日头条 微软 拼多多 英伟达
标签：数组
"""
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
	# 浅拷贝，不是真正意义的多维数组
	# res = [[0] * n] * n
	# 深拷贝
	res = [[0] * n for _ in range(n)]
	left, up = 0, 0
	right, down = n - 1, n - 1
	num = 1
	while True:
		# 向右
		i = left
		while i <= right:
			res[up][i] = num
			i += 1
			num += 1
		# 重新定义上边界
		up += 1
		if up > down:
			break

		# 向下
		i = up
		while i <= down:
			res[i][right] = num
			i += 1
			num += 1
		# 重新定义右边界
		right -= 1
		if right < left:
			break

		# 向左
		i = right
		while i >= left:
			res[down][i] = num
			i -= 1
			num += 1
		# 重新定义下边界
		down -= 1
		if down < up:
			break

		# 向上
		i = down
		while i >= up:
			res[i][left] = num
			i -= 1
			num += 1
		# 重新定义左边界
		left += 1
		if left > right:
			break

	return res


if __name__ == '__main__':
	input = 4
	result = generateMatrix(input)
	print(result)
