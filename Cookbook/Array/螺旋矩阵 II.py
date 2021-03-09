'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 20
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n - 1, 0, n - 1
        res = [[0] * n for _ in range(n)]
        value = 1
        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                res[top][c] = value
                value += 1
            for r in range(top + 1, bottom + 1):
                res[r][right] = value
                value += 1
            if left < right and top < bottom:
                for c in range(right - 1, left, -1):
                    res[bottom][c] = value
                    value += 1
                for r in range(bottom, top, -1):
                    res[r][left] = value
                    value += 1
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res


if __name__ == '__main__':
    n = 4
    sol = Solution()
    print(sol.generateMatrix(n))
