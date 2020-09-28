"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = Counter(s)
        flag = False
        for v in count.values():
            if v % 2 == 1 and not flag:
                flag = True
                res += 1
            res += v // 2 * 2
        return res


if __name__ == '__main__':
    s = "abccccdd"
    sol = Solution()
    print(sol.longestPalindrome(s))
