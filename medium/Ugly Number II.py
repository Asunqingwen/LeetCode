# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 17:13
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Ugly Number II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


def nthUglyNumber(n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    l_2, l_3, l_5 = 0, 0, 0
    for i in range(1, n):
        dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
        if dp[i] >= 2 * dp[l_2]:
            l_2 += 1
        if dp[i] >= 3 * dp[l_3]:
            l_3 += 1
        if dp[i] >= 5 * dp[l_5]:
            l_5 += 1
    return dp[-1]


if __name__ == '__main__':
    n = 100
    result = nthUglyNumber(n)
    print(result)
