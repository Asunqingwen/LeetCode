"""
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:

字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。
"""
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        len_s = len(S)
        ans = [0] * len_s
        pre_C = 10000
        for i in range(len_s):
            if S[i] == C:
                pre_C = i
            ans[i] = abs(i - pre_C)
        pre_C = 10000
        for i in range(len_s - 1, -1, -1):
            if S[i] == C:
                pre_C = i
            ans[i] = min(ans[i], abs(i - pre_C))
        return ans


if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    sol = Solution()
    print(sol.shortestToChar(S, C))
