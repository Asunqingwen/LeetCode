# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 11:22
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Sum of Digits in the Minimum Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.

Return 0 if S is odd, otherwise return 1.

 

Example 1:

Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation:
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.
Example 2:

Input: [99,77,33,66,55]
Output: 1
Explanation:
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
"""
from typing import List


def sumOfDigits(A: List[int]) -> int:
	sum = min(A)
	res = 0
	while sum > 0:
		res += sum % 10
		sum //= 10
	return (res % 2) ^ 1


if __name__ == '__main__':
	input = [31, 23, 60, 29, 71, 65, 38, 49, 99, 25, 50, 93, 71, 87, 97, 54, 19, 75, 37, 27, 33, 78, 59, 19, 86, 76, 93,
	         32, 25, 23, 32, 54, 38]
	result = sumOfDigits(input)
	print(result)
