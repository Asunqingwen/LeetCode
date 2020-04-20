"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        one_list = []
        one_dict = {}
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    one_list.append((i, j))
                    one_dict[(i, j)] = 1
        result = 0
        while one_list:
            position = one_list.pop(0)
            if position not in one_dict:
                continue
            stack = [position]
            while stack:
                i, j = stack.pop(0)
                for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == "1" and (r, c) in one_dict:
                        stack.append((r, c))
                        del one_dict[(r, c)]
            result += 1
        return result


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
    sol = Solution()
    result = sol.numIslands(grid)
    print(result)
