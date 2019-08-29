# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 14:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rotated Digits.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].

企业：今日头条 Adobe 谷歌
标签：字符串
"""


def rotatedDigits(N: int) -> int:
	nums = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
	count = 0
	for i in range(1, N + 1):
		str_num = str(i)
		temp_num = ''
		for s in str_num:
			if s not in nums:
				break
			temp_num += nums[s]
		if len(temp_num) == len(str_num) and temp_num != str_num:
			count += 1
	return count


if __name__ == '__main__':
	input = 10
	result = rotatedDigits(input)
	print(result)
