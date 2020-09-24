"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        l, r = 2, num // 2
        while l <= r:
            mid = (l + r) >> 1
            n = mid ** 2
            if n == num:
                return True
            elif n < num:
                l = mid + 1
            else:
                r = mid - 1
        return False


if __name__ == '__main__':
    num = 14
    sol = Solution()
    print(sol.isPerfectSquare(num))
