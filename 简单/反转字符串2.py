"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
 

提示：

该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        len_ = len(s_list)
        for i in range(0, len_, 2 * k):
            if len_ - i < k:
                s_list[i:] = s_list[i:][::-1]
                break
            s_list[i:i + k] = s_list[i:i + k][::-1]
        return ''.join(s_list)


if __name__ == '__main__':
    s = "abcdefg"
    k = 8
    sol = Solution()
    print(sol.reverseStr(s, k))
