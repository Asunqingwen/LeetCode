"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n != 0:
            n -= 1
            # 26进制
            mod = n % 26
            res = chr(mod + 65) + res
            n = n // 26
        return res


if __name__ == '__main__':
    n = 52
    sol = Solution()
    result = sol.convertToTitle(n)
    print(result)
