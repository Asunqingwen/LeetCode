'''
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。


示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            if r < 0 or r >= self.rows or c < 0 or c >= self.cols or grid[r][c] == '1':
                return
            grid[r][c] = '0'
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)

        self.rows, self.cols = len(grid), len(grid[0])
        res = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(grid, r, c)
        return res


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    sol = Solution()
    res = sol.numIslands(grid)
