'''
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 

示例 1：


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
示例 2：

输入：board = [["X"]]
输出：[["X"]]
 

提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'
'''
from typing import List


class UnionFind:
    def __init__(self, totalNodes):
        self.parents = [0] * totalNodes
        for i in range(totalNodes):
            self.parents[i] = i

    def find(self, node: int):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1: int, node2: int):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parents[root2] = root1

    def isConnected(self, node1: int, node2: int):
        return self.find(node1) == self.find(node2)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        uf = UnionFind(row * col + 1)  # 多加一个节点，边界上的O的父节点都是该节点
        dumpyNode = row * col  # 虚拟节点
        node = lambda i, j: i * col + j
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:  # 边界上的O
                        uf.union(node(i, j), dumpyNode)
                    else:
                        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            new_i, new_j = i + di, j + dj
                            if 0 < i < row - 1 and 0 < j < col - 1 and board[new_i][new_j] == 'O':
                                uf.union(node(i, j), node(new_i, new_j))

        for i in range(row):
            for j in range(col):
                if uf.isConnected(node(i, j), dumpyNode):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


if __name__ == '__main__':
    board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    sol = Solution()
    sol.solve(board)
    print(board)
