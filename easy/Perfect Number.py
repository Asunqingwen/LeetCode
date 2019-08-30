# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 14:42
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Perfect Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""


def checkPerfectNumber(num: int) -> bool:
	if num < 2:
		return False
	div_list = []
	div_list.append(1)
	for i in range(2, int(num ** 0.5) + 1):
		if num % i is 0:
			div_list.append(i)
			div_list.append(num // i)
	return sum(div_list) == num


if __name__ == '__main__':
	input = 30
	result = checkPerfectNumber(input)
	print(result)
