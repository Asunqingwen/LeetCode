"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        flag = ''
        str_x = str(x)
        if str_x[0] == '-':
            flag = '-'
            str_x = str_x[1:]
        str_x = str_x[::-1]
        i = 0
        for c in str_x:
            if c == '0':
                i += 1
            else:
                break
        res = int(str_x[i:])
        res = res if not flag else -res
        return res if -2 ** 31 <= res <= 2 ** 31 else 0


if __name__ == '__main__':
    x = 1534236469
    sol = Solution()
    result = sol.reverse(x)
    print(result)
