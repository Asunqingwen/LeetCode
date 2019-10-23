# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 0023 9:22
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: N-Queens.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
from typing import List


def solveNQueens(n: int) -> List[List[str]]:
	def helper():
		row = len(queens)
		if row == n:
			res.append(queens[:])
		for col in range(n):
			if col not in queens and xy_dif[row - col] and xy_sum[row + col]:
				queens.append(col)  # 放置棋子
				xy_dif[row - col], xy_sum[row + col] = 0, 0
				helper()  # 下一行
				queens.pop()  # 回溯
				xy_dif[row - col], xy_sum[row + col] = 1, 1

	queens = []
	xy_dif = [1] * (2 * n - 1)  # 主对角线
	xy_sum = [1] * (2 * n - 1)  # 副对角线
	res = []
	helper()
	return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]


if __name__ == '__main__':
	n = 4
	result = solveNQueens(n)
	print(result)
