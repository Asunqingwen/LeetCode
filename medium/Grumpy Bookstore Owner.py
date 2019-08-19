# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 16:14
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Grumpy Bookstore Owner.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""
from typing import List


# 超出时间限制
def maxSatisfied(customers: List[int], grumpy: List[int], X: int) -> int:
	no_ability = 0
	for i in range(len(grumpy)):
		if not grumpy[i]:
			no_ability += customers[i]
	use_ability = 0
	for i in range(len(grumpy)):
		win = grumpy[i:i + X]
		use_sum = sum([customers[i + index] for index, _ in enumerate(win) if _])
		use_ability = max(use_sum, use_ability)
	return no_ability + use_ability


def maxSatisfied1(customers: List[int], grumpy: List[int], X: int) -> int:
	no_ability = 0
	for i in range(len(grumpy)):
		if grumpy[i]:
			grumpy[i] = customers[i]
		else:
			no_ability += customers[i]

	use_ability = sum(grumpy[:X])
	use_sum = use_ability
	for i in range(X, len(grumpy)):
		use_sum = use_sum - grumpy[i - X] + grumpy[i]
		use_ability = max(use_ability, use_sum)
	return no_ability + use_ability


if __name__ == '__main__':
	customers = [1, 0, 1, 2, 1, 1, 7, 5]
	grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
	X = 3
	result = maxSatisfied1(customers, grumpy, X)
	print(result)
