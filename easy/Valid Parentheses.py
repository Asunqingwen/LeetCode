# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 15:22
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Valid Parentheses.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


def isValid(s: str) -> bool:
	par_dict = {')': '(', ']': '[', '}': '{'}
	stack = []
	for ss in s:
		if ss in par_dict:
			top_par = stack.pop() if stack else '#'
			if top_par != par_dict[ss]:
				return False
		else:
			stack.append(ss)

	return not stack

if __name__ == '__main__':
	s = "("
	result = isValid(s)
	print(result)
