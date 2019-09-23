# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 16:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Paint House II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Follow up:
Could you solve it in O(nk) runtime?
"""
from typing import List


def minCostII(costs: List[List[int]]) -> int:
	if not costs:
		return 0
	n, k = len(costs), len(costs[0])
	res = costs[0]
	for i in range(1, n):
		ans = res[:]
		for j in range(k):
			res[j] = costs[i][j] + min([tmp for index, tmp in enumerate(ans) if index != j])
	return min(res)


if __name__ == '__main__':
	input = [[19, 3, 18, 4, 13, 1, 12, 6, 3, 12, 3, 3, 9], [11, 5, 9, 16, 2, 19, 15, 10, 13, 20, 15, 2, 13],
	         [19, 6, 18, 7, 6, 10, 11, 13, 8, 19, 4, 14, 18], [3, 18, 18, 9, 3, 6, 18, 11, 7, 4, 13, 3, 12]]
	result = minCostII(input)
	print(result)
