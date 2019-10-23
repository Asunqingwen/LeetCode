# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 0023 10:47
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: N-Queens II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


def totalNQueens(n: int) -> int:
	def helper():
		nonlocal res
		row = len(queens)
		if row == n:
			res += 1
		for col in range(n):
			if col not in queens and xy_main[row - col] and xy_para[row + col]:
				queens.append(col)
				xy_main[row - col], xy_para[row + col] = 0, 0
				helper()
				queens.pop()
				xy_main[row - col], xy_para[row + col] = 1, 1

	queens = []
	xy_main = [1] * (2 * n - 1)  # 主对角线
	xy_para = [1] * (2 * n - 1)  # 副对角线
	res = 0
	helper()
	return res


if __name__ == '__main__':
	n = 4
	result = totalNQueens(n)
	print(result)
