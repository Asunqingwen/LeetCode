'''
给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。

题目数据保证总会存在一个数值和不超过 k 的矩形区域。

 

示例 1：


输入：matrix = [[1,0,1],[0,-2,3]], k = 2
输出：2
解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
示例 2：

输入：matrix = [[2,2,-1]], k = 3
输出：3
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 

进阶：如果行数远大于列数，该如何设计解决方案？
'''
from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        res = float("-inf")
        row, col = len(matrix), len(matrix[0])
        for i in range(row):  ## 枚举上边界
            total = [0] * col
            for j in range(i, row):  ## 枚举下边界
                for c in range(col):
                    total[c] += matrix[j][c]  ## 更新每列的元素和

                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        res = max(res, s - totalSet[lb])
                    totalSet.add(s)
        return res


if __name__ == '__main__':
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    sol = Solution()
    print(sol.maxSumSubmatrix(matrix, k))
