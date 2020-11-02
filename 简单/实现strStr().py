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
        def KMP(M):
            '''
            :param M:模式串长度
            :return:
            '''
            # 影子状态X，保证具有相同前缀的状态转移，回退最少，初始为0状态,相当于X在模式串内部进行KMP匹配
            X = 0
            for j in range(1, M):
                for c in range(128):
                    dp[j][c] = dp[X][c]  # 假设都没匹配上，全部回退
                dp[j][ord(needle[j])] = j + 1  # 和模式串当前字符相等的，推进到下一个状态
                # 更新影子状态
                X = dp[X][ord(needle[j])]

        N = len(haystack)
        M = len(needle)  # 状态个数，就是模式串的长度
        if M == 0:
            return 0
        # dp[状态][字符] = 下个状态
        dp = [[0] * 128 for _ in range(M)]  # 255个ascii字符，文本无特殊符号时，128就可以了
        # 初始化,初始状态为0，只有在文本中遇到模式串的第一个字符，才会转移到状态1
        dp[0][ord(needle[0])] = 1
        KMP(M)
        j = 0
        for i in range(N):
            j = dp[j][ord(haystack[i])]
            if j == M:
                return i - M + 1
        return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issip"
    sol = Solution()
    print(sol.strStr(haystack, needle))
