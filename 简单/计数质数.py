"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        res = [True] * n
        res[0:2] = [False, False]

        for i in range(2, n):
            if res[i]:
                # i为素数，i的整数倍都不为素数
                j = 2 * i
                while j < n:
                    res[j] = False
                    j += i

        return sum(res)


if __name__ == '__main__':
    n = 10
    sol = Solution()
    result = sol.countPrimes(n)
    print(result)
