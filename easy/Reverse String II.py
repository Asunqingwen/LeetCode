# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 10:52
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse String II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


def reverseStr(s: str, k: int) -> str:
	s = list(s)
	for i in range(0, len(s), 2 * k):
		s[i:i + k] = reversed(s[i:i + k])
	return ''.join(s)


if __name__ == '__main__':
	s = "abcdefgh"
	k = 3
	result = reverseStr(s, k)
	print(result)
