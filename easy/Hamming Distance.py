# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 10:19
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Hamming Distance.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


def hammingDistance(x: int, y: int) -> int:
	return bin(x ^ y).count('1')


if __name__ == '__main__':
	x = 1
	y = 4
	result = hammingDistance(x, y)
	print(result)
