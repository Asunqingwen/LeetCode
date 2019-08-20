# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 20:54
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Number Complement.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
"""


def findComplement(num: int) -> int:
    bin_sum = bin(num)[2:]
    mask = '1' * len(bin_sum)
    return int(bin_sum, 2) ^ int(mask, 2)


if __name__ == '__main__':
    input = 5
    output = findComplement(input)
    print(output)
