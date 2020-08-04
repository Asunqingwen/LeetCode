"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        win = dict()
        left, right = 0, 0
        ans = 0
        while right < len(s):
            c = s[right]
            right += 1
            win[c] = win.get(c, 0) + 1
            while len(win) > k:
                d = s[left]
                left += 1
                win[d] -= 1
                if win[d] == 0:
                    win.pop(d)
            ans = max(ans, right - left)
        return ans

if __name__ == '__main__':
    s = "eceba"
    k = 2
    sol = Solution()
    result = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(result)
