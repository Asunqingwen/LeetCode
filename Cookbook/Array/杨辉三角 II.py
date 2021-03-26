'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        if rowIndex == 1:
            return [1]
        res = [1]
        for i in range(2, rowIndex + 1):
            for j in range(i - 2):
                res[j] = res[j] + res[j + 1]
            res = [1] + res
        return res


if __name__ == '__main__':
    rowIndex = 3
    sol = Solution()
    print(sol.getRow(rowIndex))
