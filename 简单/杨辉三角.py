"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [1] * (numRows)
        res = []
        for i in range(numRows):
            for j in range(i - 1, 0, -1):
                ans[j] = ans[j] + ans[j - 1]
            res.append(ans[0:i+1])
        return res


if __name__ == '__main__':
    numRows = 5
    sol = Solution()
    result = sol.generate(numRows)
    print(result)
