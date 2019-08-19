# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 0018 10:24
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: To Lower Case.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""


def toLowerCase(str: str) -> str:
	return str.lower()

if __name__ == '__main__':
	str = "Hello"
	result = toLowerCase(str)
	print(result)
