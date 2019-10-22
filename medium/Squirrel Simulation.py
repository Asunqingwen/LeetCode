# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 0022 9:32
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Squirrel Simulation.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
Example 1:

Input:
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:
​​​​​
Note:

All given positions won't overlap.
The squirrel can take at most one nut at one time.
The given positions of nuts have no order.
Height and width are positive integers. 3 <= height * width <= 10,000.
The given positions contain at least one nut, only one tree and one squirrel.
"""
from typing import List


def minDistance(height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
	max_dd, res = float('-inf'), 0
	for nut in nuts:
		tree_dd = abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])
		squirrel_dd = abs(squirrel[0] - nut[0]) + abs(squirrel[1] - nut[1])
		max_dd = max(max_dd, tree_dd - squirrel_dd)
		res += 2 * tree_dd
	return res - max_dd


if __name__ == '__main__':
	height = 5
	width = 7
	tree = [2, 2]
	squirrel = [4, 2]
	nuts = [[4, 3], [2, 6]]
	result = minDistance(height, width, tree, squirrel, nuts)
	print(result)
