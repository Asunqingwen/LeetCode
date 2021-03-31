'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

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
'''
from typing import List

class UnionFind:
    def __init__(self,grid):
        row, col = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (row * col)
        self.rank = [0] * (row * col)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.parent[i * col + j] = i * col + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  #路径压缩
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:  #将秩，即树的深度小的父节点设为深度大的节点
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1   #合并一个节点，就少一个岛

    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        uf = UnionFind(grid)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                            uf.union(r * col + c, x * col + y)
        return uf.getCount()


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    sol = Solution()
    print(sol.numIslands(grid))
