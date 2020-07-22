"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(head=1, curr=[]):
            if len(curr) == k:
                res.append(curr[:])
                return  # 剪枝
            for i in range(head, n + 1):
                curr.append(i)
                helper(i + 1, curr)
                curr.pop()

        helper()
        return res


if __name__ == '__main__':
    n = 4
    k = 2
    sol = Solution()
    result = sol.combine(n, k)
    print(result)
