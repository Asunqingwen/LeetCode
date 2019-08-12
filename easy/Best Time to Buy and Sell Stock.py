# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 0006 16:39
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Best Time to Buy and Sell Stock.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
	size = len(prices)
	if size <= 1:
		return 0
	min_price = prices[0]
	max_profit = 0
	for i in range(1, len(prices)):
		if prices[i] < min_price:
			min_price = prices[i]
		else:
			temp_profit = prices[i] - min_price
			if temp_profit > max_profit:
				max_profit = temp_profit
	return max_profit


def maxProfit1(prices: List[int]) -> int:
	dp_i_1 = float('-inf')
	dp_i_0 = 0
	for i in range(len(prices)):
		dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
		dp_i_1 = max(dp_i_1, -prices[i])
	return dp_i_0


if __name__ == '__main__':
	nums = [7,1,5,3,6,4]
	result = maxProfit1(nums)
	print(result)
