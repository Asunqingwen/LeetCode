'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, col - 1, 0, row - 1
        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            for r in range(top + 1, bottom + 1):
                res.append(matrix[r][right])
            if left < right and top < bottom:
                for c in range(right - 1, left, -1):
                    res.append(matrix[bottom][c])
                for r in range(bottom, top, -1):
                    res.append(matrix[r][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    print(sol.spiralOrder(matrix))
