# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 0007 9:22
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Best Time to Buy and Sell Stock II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
	dp_i_1 = float('-inf')
	dp_i_0 = 0
	for i in range(len(prices)):
		temp = dp_i_0
		dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
		dp_i_1 = max(dp_i_1, temp - prices[i])
	return dp_i_0


if __name__ == '__main__':
	nums = [7, 1, 5, 3, 6, 4]
	result = maxProfit(nums)
	print(result)
