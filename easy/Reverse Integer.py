# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 13:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse Integer.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def reverse(x: int) -> int:
	s = str(x)[::-1].rstrip('-')
	if int(s) < 2 ** 31:
		if x >= 0:
			return int(s)
		else:
			return 0 - int(s)
	return 0

if __name__ == '__main__':
	nums = 123
	result = reverse(nums)
	print(result)