"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        zeroes_pos = [(i, j) for i in range(row) for j in range(col) if matrix[i][j] == 0]
        result = [[0] * col for _ in range(row)]
        seen = set(zeroes_pos)
        while zeroes_pos:
            i, j = zeroes_pos.pop(0)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < row and 0 <= nj < col and (ni, nj) not in seen:
                    result[ni][nj] = result[i][j] + 1
                    zeroes_pos.append((ni, nj))
                    seen.add((ni, nj))
        return result


if __name__ == '__main__':
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    sol = Solution()
    result = sol.updateMatrix(matrix)
    print(result)
