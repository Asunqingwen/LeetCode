# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 14:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Self Dividing Numbers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
from typing import List


def selfDividingNumbers(left: int, right: int) -> List[int]:
	result = []
	for num in range(left, right + 1):
		num_str = str(num)
		i = 0
		while i < len(num_str):
			if int(num_str[i]) is 0 or num % int(num_str[i]) is not 0:
				break
			i += 1
		if i is len(num_str):
			result.append(num)
	return result


if __name__ == '__main__':
	left = 1
	right = 22
	result = selfDividingNumbers(left, right)
	print(result)
