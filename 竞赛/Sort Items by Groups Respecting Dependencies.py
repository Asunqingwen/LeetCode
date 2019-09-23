# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 16:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Sort Items by Groups Respecting Dependencies.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.



Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.



Constraints:

1 <= m <= n <= 3*10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m-1
0 <= beforeItems[i].length <= n-1
0 <= beforeItems[i][j] <= n-1
i != beforeItems[i][j]
"""
from queue import Queue
from typing import List

import numpy as np


def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
	# 组内拓扑排序
	def get_group_ans(group_points, group_edges):
		# 组内级别建图
		graph = {group_point: [] for group_point in group_points}
		degree = {group_point: 0 for group_point in group_points}
		for x, y in group_edges:
			graph[y].append(x)
			degree[x] += 1
		# top sort
		q = Queue()
		for graph_point in group_points:
			if degree[graph_point] == 0:
				q.put(graph_point)

		# 组内拓扑排序
		task_res = []
		while not q.empty():
			x = q.get()
			task_res.append(x)
			for y in graph[x]:
				degree[y] -= 1
				if degree[y] == 0:
					q.put(y)
		if len(task_res) != len(group_points):
			return None
		return task_res

	group_cnt = max(group) + 1
	for i in range(n):
		if group[i] == -1:
			group[i] = group_cnt
			group_cnt += 1
	# 组级别建图
	group_ids = np.unique(group)
	graph = {group_id: [] for group_id in group_ids}
	degree = {group_id: 0 for group_id in group_ids}
	group_inner_edges = {group_id: [] for group_id in group_ids}
	group_points = {group_id: [] for group_id in group_ids}
	for i in range(n):
		groupa = group[i]
		group_points[groupa].append(i)
		for j in beforeItems[i]:
			groupb = group[j]
			if groupa == groupb:
				group_inner_edges[groupa].append([i, j])
				continue
			graph[groupb].append(groupa)
			degree[groupa] += 1

	# 组级别拓扑排序
	q = Queue()
	for group_id in group_ids:
		if degree[group_id] == 0:
			q.put(group_id)
	group_res = []
	while not q.empty():
		x = q.get()
		group_res.append(x)
		for y in graph[x]:
			degree[y] -= 1
			if degree[y] == 0:
				q.put(y)

	if len(group_res) != len(group_ids):
		return []
	# 根据组拓扑序整合结果
	task_res = []
	for group_id in group_res:
		ans = get_group_ans(group_points[group_id], group_inner_edges[group_id])
		if ans is None:
			return []
		task_res += ans
	return task_res


if __name__ == '__main__':
	n = 8
	m = 2
	group = [-1, -1, 1, 0, 0, 1, 0, -1]
	beforeItems = [[], [6], [5], [6], [3], [], [4], []]
	result = sortItems(n, m, group, beforeItems)
	print(result)
