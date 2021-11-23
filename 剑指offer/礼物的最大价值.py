from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        for i in range(1, cols):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for j in range(1, rows):
            grid[j][0] = grid[j - 1][0] + grid[j][0]
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 2, 3], [4, 5, 6]]
    sol.maxValue(grid)
