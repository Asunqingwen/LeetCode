"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        l, r, u, d, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            # 从左到右
            for i in range(l, r + 1): res.append(matrix[u][i])
            u += 1
            if u > d: break
            # 从上到下
            for i in range(u, d + 1): res.append(matrix[i][r])
            r -= 1
            if l > r: break
            # 从右到左
            for i in range(r, l - 1, -1): res.append(matrix[d][i])
            d -= 1
            if u > d: break
            # 从下到上
            for i in range(d, u - 1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    result = sol.spiralOrder(matrix)
    print(result)
