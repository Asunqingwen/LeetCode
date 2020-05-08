"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxEdge = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i and j:
                    if matrix[i][j] == "1":
                        matrix[i][j] = min(int(matrix[i - 1][j - 1]), int(matrix[i][j - 1]), int(matrix[i - 1][j])) + 1
                    else:
                        matrix[i][j] = 0
                maxEdge = max(maxEdge, int(matrix[i][j]))
        return maxEdge ** 2


if __name__ == '__main__':
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    sol = Solution()
    result = sol.maximalSquare(matrix)
    print(result)
