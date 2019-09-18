# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 0018 15:23
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 1-bit and 2-bit Characters.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
"""
from typing import List


def isOneBitCharacter(bits: List[int]) -> bool:
	parity = bits.pop()
	while bits and bits.pop():
		parity ^= 1
	return parity == 0

if __name__ == '__main__':
	bits = [1, 0,0, 0]
	result = isOneBitCharacter(bits)
	print(result)
