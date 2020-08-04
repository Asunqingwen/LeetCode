"""
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        win = dict()
        left, right = 0, 0
        ans = 0
        while right < len(s):
            c = s[right]
            right += 1
            win[c] = win.get(c, 0) + 1
            while len(win) > 2:
                d = s[left]
                left += 1
                win[d] -= 1
                if win[d] == 0:
                    win.pop(d)
            ans = max(ans, right - left)
        return ans


if __name__ == '__main__':
    s = "ccaabbb"
    sol = Solution()
    result = sol.lengthOfLongestSubstringTwoDistinct(s)
    print(result)
