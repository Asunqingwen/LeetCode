# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 13:50
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Flip Game.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output:
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
"""
from typing import List


def generatePossibleNextMoves(s: str) -> List[str]:
	res = []
	for i in range(len(s) - 1):
		if s[i:i+2] == '++':
			left = s[:i]
			right = s[i + 2:]
			res.append(left + '--' + right)

	return res


if __name__ == '__main__':
	s = "++++"
	result = generatePossibleNextMoves(s)
	print(result)
