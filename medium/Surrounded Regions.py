# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 0030 14:24
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Surrounded Regions.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
from typing import List


def solve(board: List[List[str]]) -> None:
	if not board:
		return
	row, col = len(board), len(board[0])
	res = []
	for j in range(col):
		if board[0][j] == 'O':
			board[0][j] = '1'
			res.append([0, j])
		if board[row - 1][j] == 'O':
			board[row - 1][j] = '1'
			res.append([row - 1, j])
	for i in range(1, row - 1):
		if board[i][0] == 'O':
			board[i][0] = '1'
			res.append([i, 0])
		if board[i][col - 1] == 'O':
			board[i][col - 1] = '1'
			res.append([i, col - 1])
	while res:
		i, j = res.pop(0)
		left, right, up, down = j - 1, j + 1, i - 1, i + 1
		if left >= 0 and board[i][left] == 'O':
			board[i][left] = '1'
			res.append([i, left])
		if right < col and board[i][right] == 'O':
			board[i][right] = '1'
			res.append([i, right])
		if up >= 0 and board[up][j] == 'O':
			board[up][j] = '1'
			res.append([up, j])
		if down < row and board[down][j] == 'O':
			board[down][j] = '1'
			res.append([down, j])
	for i in range(row):
		for j in range(col):
			if board[i][j] == '1':
				board[i][j] = 'O'
			else:
				board[i][j] = 'X'


if __name__ == '__main__':
	input = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
	solve(input)
	print(input)
