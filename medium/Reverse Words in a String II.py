# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 15:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse Words in a String II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

企业：微软 亚马逊 优步
标签：字符串
"""
from typing import List


def reverseWords(s: List[str]) -> None:
	head, tail = 0, len(s) - 1
	while head < tail:
		s[head], s[tail] = s[tail], s[head]
		head, tail = head + 1, tail - 1
	head, tail = 0, 0
	size = len(s)
	for index in range(size):
		if index + 1 == size or s[index + 1] == ' ':
			tail = index
			while head < tail:
				s[head], s[tail] = s[tail], s[head]
				head, tail = head + 1, tail - 1
			head = index + 2


def reverseWords1(s: List[str]) -> None:
	s[:] = ' '.join(''.join(s).split()[::-1])


if __name__ == '__main__':
	input = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
	reverseWords(input)
	print(input)
