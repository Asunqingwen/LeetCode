# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 10:40
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


def reverseString(s: List[str]) -> None:
	"""
	Do not return anything, modify s in-place instead.
	"""
	left, right = 0, len(s) - 1
	while left <= right:
		s[left], s[right] = s[right], s[left]
		left += 1
		right -= 1


if __name__ == '__main__':
	input = ['']
	result = reverseString(input)
	print(input)
