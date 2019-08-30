# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 9:06
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Robot Return to Origin.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

Example 1:

Input: "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
"""


def judgeCircle(moves: str) -> bool:
	LR_count = 0
	UD_count = 0
	move_dict = {'L': 1, 'R': -1, 'U': 1, 'D': -1}
	for m in moves:
		if m in ['L', 'R']:
			LR_count += move_dict[m]
		else:
			UD_count += move_dict[m]
	return not LR_count and not UD_count


def judgeCircle1(moves: str) -> bool:
	return moves.count('L') == moves.count('R') and moves.count('D') == moves.count('U')


if __name__ == '__main__':
	input = "LDRRLRUULR"
	result = judgeCircle(input)
	print(result)
