# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 14:38
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Flip Game II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.
"""


def canWin(s: str) -> bool:
	for i in range(len(s)-1):
		if s[i:i+2] == '++':
			ans = s[:i]+'--'+s[i+2:]
			if canWin(ans):
				return True
	return True


if __name__ == '__main__':
	s = "++++"
	result = canWin(s)
	print(result)