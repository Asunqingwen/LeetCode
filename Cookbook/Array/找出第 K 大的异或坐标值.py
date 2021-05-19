'''
给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。

矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。

请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。

 

示例 1：

输入：matrix = [[5,2],[1,6]], k = 1
输出：7
解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
示例 2：

输入：matrix = [[5,2],[1,6]], k = 2
输出：5
解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
示例 3：

输入：matrix = [[5,2],[1,6]], k = 3
输出：4
解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
示例 4：

输入：matrix = [[5,2],[1,6]], k = 4
输出：0
解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n
'''
import operator
from random import random
from typing import List, Callable


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        results = list()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                results.append(pre[i][j])

        def nth_element(left: int, kth: int, right: int, op: Callable[[int, int], bool]):
            if left == right:
                return

            pivot = random.randint(left, right)
            results[pivot], results[right] = results[right], results[pivot]

            # 三路划分（three-way partition）
            sepl = sepr = left - 1
            for i in range(left, right + 1):
                if op(results[i], results[right]):
                    sepr += 1
                    if sepr != i:
                        results[sepr], results[i] = results[i], results[sepr]
                    sepl += 1
                    if sepl != sepr:
                        results[sepl], results[sepr] = results[sepr], results[sepl]
                elif results[i] == results[right]:
                    sepr += 1
                    if sepr != i:
                        results[sepr], results[i] = results[i], results[sepr]

            if sepl < left + kth <= sepr:
                return
            elif left + kth <= sepl:
                nth_element(left, kth, sepl, op)
            else:
                nth_element(sepr + 1, kth - (sepr - left + 1), right, op)

        nth_element(0, k - 1, len(results) - 1, operator.gt)
        return results[k - 1]


if __name__ == '__main__':
    matrix = [[5, 2], [1, 6]]
    k = 1
    sol = Solution()
    print(sol.kthLargestValue(matrix, k))
