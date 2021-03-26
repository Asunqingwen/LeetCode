'''
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
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(2, numRows + 1):
            ans = [1]
            for j in range(1, i - 1):
                ans.append(res[-1][j - 1] + res[-1][j])
            ans += [1]
            res.append(ans[:])
        return res


if __name__ == '__main__':
    numRows = 5
    sol = Solution()
    print(sol.generate(numRows))
