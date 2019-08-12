# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 14:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Narcissistic Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits. See wiki

For example the 3-digit decimal number 153 is a narcissistic number because 153 = 13 + 53 + 33.

And the 4-digit decimal number 1634 is a narcissistic number because 1634 = 14 + 64 + 34 + 44.

Given n, return all narcissistic numbers with n digits.
"""


def getNarcissisticNumbers(n):
	list_n = []
	for i in range(10 ** (n - 1), 10 ** n):
		str_n = str(i)
		str_n = list(str_n)
		pow_n = len(str_n)
		str_n = sum([int(i) ** pow_n for i in str_n])
		if i == str_n:
			list_n.append(i)
	if n == 1:
		list_n = [0] + list_n
	return list_n


if __name__ == '__main__':
	n = 6
	result = getNarcissisticNumbers(n)
	print(result)
