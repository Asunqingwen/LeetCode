# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 15:56
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: X of a Kind in a Deck of Cards.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
相关企业：无
标签：数组 数学
"""
import collections
from typing import List


def hasGroupsSizeX(deck: List[int]) -> bool:
	count_dict = {}
	for num in deck:
		count_dict[num] = count_dict.get(num, 0) + 1
	size = len(count_dict)
	min_value = min(count_dict.values())
	if min_value < 2:
		return False
	for X in range(min_value + 1, 1, -1):
		count = 0
		for value in count_dict.values():
			if value % X != 0:
				break
			count += 1
		if count == size:
			return True
	return False


def hasGroupsSizeX1(deck: List[int]) -> bool:
	count = collections.Counter(deck)
	min_value = min(count.values())
	if min_value < 2:
		return False
	for i in range(min_value + 1, 1, -1):
		result = all(value % i == 0 for value in count.values())
		if result:
			return True
	return False


if __name__ == '__main__':
	input = [1]
	result = hasGroupsSizeX(input)
	print(result)
