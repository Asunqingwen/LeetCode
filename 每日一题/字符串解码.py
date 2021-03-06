"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                temp = ''
                # 字母多于1个
                while stack[-1].isalpha():
                    temp = stack.pop(-1) + temp
                stack.pop(-1)
                count = ''
                # 数字超过10
                while stack and stack[-1].isnumeric():
                    count = stack.pop(-1) + count
                for j in range(int(count)):
                    stack.append(temp)
            else:
                stack.append(s[i])
        return ''.join(stack)


if __name__ == '__main__':
    s = "10[a]"
    sol = Solution()
    result = sol.decodeString(s)
    print(result)
