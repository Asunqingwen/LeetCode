"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        len_a, len_b = len(A), len(B)
        dp = [0] * (len_b + 1)
        for i in range(len_a):
            for j in range(len_b - 1, -1, -1):
                if A[i] == B[j]:
                    dp[j] = dp[j - 1] + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
        return res


if __name__ == '__main__':
    A = [0, 0, 0, 0, 1]
    B = [1, 0, 0, 0, 0]
    sol = Solution()
    result = sol.findLength(A, B)
    print(result)
