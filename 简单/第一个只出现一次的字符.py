'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：

0 <= s 的长度 <= 50000
'''


class Solution:
    def firstUniqChar(self, s: str) -> str:
        bool_ = dict()
        for c in s:
            bool_[c] = not c in bool_
        for k in bool_:
            if bool_[k]:
                return k
        return " "

if __name__ == '__main__':
    s = "abaccdeff"
    sol = Solution()
    print(sol.firstUniqChar(s))
