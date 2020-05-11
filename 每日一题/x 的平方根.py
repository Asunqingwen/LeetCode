"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        left_num, right_num = 1, x // 2
        while left_num <= right_num:
            mid_num = left_num + (right_num - left_num) // 2
            square_num = mid_num ** 2
            square_num1 = (mid_num - 1) ** 2
            square_num2 = (mid_num + 1) ** 2
            if square_num == x or square_num < x < square_num2:
                return mid_num
            elif square_num1 < x < square_num:
                return mid_num - 1
            elif square_num > x:
                right_num = mid_num - 1
            else:
                left_num = mid_num + 1
        return left_num


if __name__ == '__main__':
    x = 4
    sol = Solution()
    result = sol.mySqrt(8)
    print(result)
