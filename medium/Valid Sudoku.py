# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 0023 11:00
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Valid Sudoku.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
from typing import List

import numpy as np


def isValidSudoku(board: List[List[str]]) -> bool:
	board = np.array(board)
	dict_row = [[0] * 10 for _ in range(10)]
	dict_col = [[0] * 10 for _ in range(10)]
	for i in range(9):
		for j in range(9):
			if board[i][j] != '.':
				index = int(board[i][j])
				dict_row[i][index] += 1
				dict_col[j][index] += 1
	for i in range(3):
		for j in range(3):
			dict99 = [0] * 10
			num99 = board[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3]
			for m in range(3):
				for n in range(3):
					if num99[m][n] != '.':
						index = int(num99[m][n])
						dict99[index] += 1
			for m in range(3):
				for n in range(3):
					if num99[m][n] == '.':
						continue
					index = int(num99[m][n])
					if dict99[index] > 1 or dict_row[i * 3 + m][index] > 1 or dict_col[j * 3 + n][index] > 1:
						return False
	return True


def isValidSudoku1(board: List[List[str]]) -> bool:
	dict_row = [{} for _ in range(9)]
	dict_col = [{} for _ in range(9)]
	dict_33 = [{} for _ in range(9)]
	for row in range(9):
		for col in range(9):
			if board[row][col] != '.':
				num = int(board[row][col])

				dict_row[row][num] = dict_row[row].get(num, 0) + 1
				dict_col[col][num] = dict_col[col].get(num, 0) + 1
				index_33 = row // 3 * 3 + col // 3
				dict_33[index_33][num] = dict_33[index_33].get(num, 0) + 1

				if dict_row[row][num] > 1 or dict_col[col][num] > 1 or dict_33[index_33][num] > 1:
					return False
	return True


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
	result = isValidSudoku1(board)
	print(result)
