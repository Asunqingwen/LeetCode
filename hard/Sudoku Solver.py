# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 0023 14:13
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Sudoku Solver.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""
from collections import defaultdict
from typing import List


def solveSudoku(board: List[List[str]]) -> None:
	def place_number(d, row, col):
		rows[row][d] += 1
		cols[col][d] += 1
		boxes[box_index(row, col)][d] += 1
		board[row][col] = str(d)

	def place_next_number(row, col):
		if row == 8 and col == 8:
			nonlocal flag
			flag = True
		else:
			if col == 8:
				helper(row + 1, 0)
			else:
				helper(row, col + 1)

	def could_place(d, row, col):
		return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])

	def remove_number(d, row, col):
		del rows[row][d]
		del cols[col][d]
		del boxes[box_index(row, col)][d]
		board[row][col] = '.'

	def helper(row=0, col=0):
		if board[row][col] == '.':
			for d in range(1, 10):
				if could_place(d, row, col):
					place_number(d, row, col)
					place_next_number(row, col)
					if not flag:
						remove_number(d, row, col)
		else:
			place_next_number(row, col)

	box_index = lambda row, col: (row // 3) * 3 + col // 3
	rows = [defaultdict(int) for _ in range(9)]
	cols = [defaultdict(int) for _ in range(9)]
	boxes = [defaultdict(int) for _ in range(9)]
	for row in range(9):
		for col in range(9):
			if board[row][col] != '.':
				place_number(int(board[row][col]), row, col)

	flag = False
	helper()


if __name__ == '__main__':
	board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
	         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
	         [".", "9", "8", ".", ".", ".", ".", "6", "."],
	         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
	         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
	         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
	         [".", "6", ".", ".", ".", ".", "2", "8", "."],
	         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
	         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
	solveSudoku(board)
	print(board)
