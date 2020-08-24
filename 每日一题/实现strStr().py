"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if n == 0:
            return 0
        ph = 0
        while ph < h - n + 1:
            while ph < h - n + 1 and haystack[ph] != needle[0]:
                ph += 1
            pn = 0
            while ph < h and pn < n and haystack[ph] == needle[pn]:
                pn += 1
                ph += 1
            # 匹配
            if pn == n:
                return ph - pn
            # 不匹配
            ph = ph - pn + 1

        return -1


if __name__ == '__main__':
    haystack = "aaaaa"
    needle = "aa"
    sol = Solution()
    result = sol.strStr(haystack, needle)
    print(result)
