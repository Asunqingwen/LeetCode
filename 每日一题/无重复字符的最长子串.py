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
    def lengthOfLongestSubstring1(self, s: str) -> int:
        length = 0
        s_dict = dict()
        result = 0
        i = 0
        while i < len(s):
            if s[i] not in s_dict:
                s_dict[s[i]] = i
                length += 1
            else:
                i = s_dict[s[i]] + 1
                if i >= len(s):
                    break
                result = max(result, length)
                s_dict.clear()
                s_dict[s[i]] = i
                length = 1
            i += 1
        return max(length, result)

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        s_set = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        right, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                s_set.remove(s[i - 1])
            while right + 1 < n and s[right + 1] not in s_set:
                # 不断地移动右指针
                s_set.add(s[right + 1])
                right += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, right - i + 1)
        return ans


if __name__ == '__main__':
    s = "dvdf"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)
