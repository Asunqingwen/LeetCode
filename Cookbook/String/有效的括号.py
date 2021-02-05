'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
'''


class Solution:
    def isValid(self, s: str) -> bool:
        len_ = len(s)
        if len_ & 1 == 1:
            return False
        dict_ = {"(": ")", "{": "}", "[": "]"}
        stack = list()
        for c in s:
            if c not in dict_:
                if not stack or dict_[stack[-1]] != c:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack


if __name__ == '__main__':
    s = "()[]{}"
    sol = Solution()
    print(sol.isValid(s))
