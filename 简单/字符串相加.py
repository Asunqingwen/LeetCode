"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

 

提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1l, num2l = len(num1), len(num2)
        if num1l < num2l:
            num1, num2 = num2, num1
            num1l, num2l = num2l, num1l
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ''
        i, j = 0, 0
        dd = 0
        while i < num1l and j < num2l:
            tmp = int(num1[i]) + int(num2[i]) + dd
            curr = tmp % 10
            dd = tmp // 10
            res = str(curr) + res
            i += 1
            j += 1
        while i < num1l:
            tmp = int(num1[i]) + dd
            curr = tmp % 10
            dd = tmp // 10
            res = str(curr) + res
            i += 1
        if dd > 0:
            res = str(dd) + res
        return res


if __name__ == '__main__':
    num1 = '1234'
    num2 = '34'
    sol = Solution()
    result = sol.addStrings(num1, num2)
    print(result)
