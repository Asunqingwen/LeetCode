"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0
        len_ = len(s)
        if len_ < 2:
            return True
        for i in range(0, len_ - 2):
            if s[i] == s[i + 1] == s[i + 2] == 'L':
                return False
            if s[i] == 'A':
                A_count += 1
            if A_count > 1:
                return False
        for i in range(len_ - 2, len_):
            if s[i] == 'A':
                A_count += 1
            if A_count > 1:
                return False
        return True


if __name__ == '__main__':
    s = 'A'
    sol = Solution()
    print(sol.checkRecord(s))
