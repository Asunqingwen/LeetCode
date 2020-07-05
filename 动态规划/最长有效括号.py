"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left + right)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for char in reversed(s):
            if char == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left + right)
            elif right < left:
                left, right = 0, 0
        return res


if __name__ == '__main__':
    s = "(()"
    sol = Solution()
    result = sol.longestValidParentheses(s)
    print(result)
