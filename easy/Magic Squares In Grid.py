# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 9:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Magic Squares In Grid.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""
from typing import List


def numMagicSquaresInside(grid: List[List[int]]) -> int:
	def helper(data):
		count = {}
		for d in data:
			count[d] = count.get(d, 0) + 1
		for i in range(1, 10):
			if i not in count:
				return False
		return data[0] + data[1] + data[2] == 15 and \
		       data[3] + data[4] + data[5] == 15 and \
		       data[6] + data[7] + data[8] == 15 and \
		       data[0] + data[3] + data[6] == 15 and \
		       data[1] + data[4] + data[7] == 15 and \
		       data[2] + data[5] + data[8] == 15 and \
		       data[0] + data[4] + data[8] == 15 and \
		       data[2] + data[4] + data[6] == 15

	row, col = len(grid), len(grid[0])
	count = 0
	for i in range(row - 2):
		for j in range(col - 2):
			if grid[i + 1][j + 1] != 5:
				continue
			ans = grid[i][j:j + 3]
			ans.extend(grid[i + 1][j:j + 3])
			ans.extend(grid[i + 2][j:j + 3])
			if helper(ans):
				count += 1
	return count


if __name__ == '__main__':
	input = [[1, 8, 6], [10, 5, 0], [4, 2, 9]]
	result = numMagicSquaresInside(input)
	print(result)
