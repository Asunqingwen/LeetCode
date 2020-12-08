'''
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100
0 <= len(s2) <= 100
'''
from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        counts = Counter(s1)
        for c in s2:
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True


if __name__ == '__main__':
    s1 = "abc"
    s2 = "bca"
    sol = Solution()
    print(sol.CheckPermutation(s1, s2))
