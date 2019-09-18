# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 0018 14:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Two City Scheduling.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""
from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
	N = len(costs)//2
	city = {index: cost[0] - cost[1] for index, cost in enumerate(costs)}
	city = sorted(city.items(), key=lambda x: x[1])
	total = 0
	for i in range(N):
		total += costs[city[i][0]][0] + costs[city[i + N][0]][1]
	return total


if __name__ == '__main__':
	input = [[10, 20], [30, 200], [400, 50], [30, 20]]
	result = twoCitySchedCost(input)
	print(result)
