"""
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = True
        if num < 0:
            flag = False
            num = abs(num)
        res = ''
        div, mod = divmod(num, 7)
        res = str(mod) + res
        while div > 0:
            div, mod = divmod(div, 7)
            res = str(mod) + res
        return res if flag else '-' + res


if __name__ == '__main__':
    num = -7
    sol = Solution()
    print(sol.convertToBase7(num))
