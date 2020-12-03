'''
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。
'''


class Solution:
    def isUnique(self, astr: str) -> bool:
        # 位运算，状态压缩
        ans = 0
        for c in astr:
            bit = 1 << int(ord(c) - ord('a'))
            if ans & bit:  # 此bit位已有数字
                return False
            else:
                ans |= bit  # 此bit位有数字，置1
        return True


if __name__ == '__main__':
    s = "leetcode"
    sol = Solution()
    print(sol.isUnique(s))
