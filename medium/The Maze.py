# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 0030 15:06
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: The Maze.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
from typing import List


def hasPath(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
	row, col = len(maze), len(maze[0])
	# 上，下，左，右
	moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	visited = set()
	ans = [start]
	visited.add(tuple(start))
	while ans:
		r, c = ans.pop(0)
		if [r, c] == destination:
			return True
		for move in moves:
			i, j = r, c
			while 0 <= i + move[0] < row and 0 <= j + move[1] < col and not maze[i + move[0]][j + move[1]]:
				i += move[0]
				j += move[1]
			if i == r and j == c:
				continue
			if (i, j) not in visited:
				ans.append((i, j))
				visited.add((i,j))
	return False


if __name__ == '__main__':
	maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
	start = [0, 4]
	destination = [3, 2]
	result = hasPath(maze, start, destination)
	print(result)
