"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
"""


class Solution:
    def sumNums(self, n: int) -> int:
        def add(n):
            return n > 0 and n + add(n - 1)

        return add(n)

    def sumNums1(self, n: int) -> int:
        return sum(range(1, n + 1))


if __name__ == '__main__':
    n = 9
    sol = Solution()
    result = sol.sumNums(n)
    print(result)
