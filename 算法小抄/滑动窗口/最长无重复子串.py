"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = dict()
        ans = 0
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            win[c] = win.get(c, 0) + 1
            # 左侧窗口是否需要收缩
            while win.get(c, 0) > 1:
                d = s[left]
                left += 1
                win[d] -= 1
            ans = max(ans, right - left)
        return ans


if __name__ == '__main__':
    s = "pwwkew"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)
