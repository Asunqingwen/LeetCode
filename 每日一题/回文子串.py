"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        length = len(s)
        for i in range(length):
            # 回文串长度为奇数
            left, right = i, i
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            # 回文串长度为偶数
            left, right = i, i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1

        return res


if __name__ == '__main__':
    s = "abc"
    sol = Solution()
    result = sol.countSubstrings(s)
    print(result)
