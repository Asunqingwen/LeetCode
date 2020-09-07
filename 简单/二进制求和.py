"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        al, bl = len(a), len(b)
        if al < bl:
            a, b = b, a
            al, bl = bl, al
        a = a[::-1]
        b = b[::-1]
        res = ''
        i, j = 0, 0
        dd = 0
        while i < al and j < bl:
            tmp = int(a[i]) + int(b[i]) + dd
            curr = tmp % 2
            dd = tmp // 2
            res = str(curr) + res
            i += 1
            j += 1
        while i < al:
            tmp = int(a[i]) + dd
            curr = tmp % 2
            dd = tmp // 2
            res = str(curr) + res
            i += 1
        if dd == 1:
            res = '1' + res
        return res


if __name__ == '__main__':
    a = '100'
    b = '110010'
    sol = Solution()
    result = sol.addBinary(a, b)
    print(result)
