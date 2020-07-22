"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

 

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
 

说明:
你可以认为每种硬币的数量是无限的
"""
from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            res = math.inf
            for coin in coins:
                if i - coin < 0:
                    continue
                res = min(res, dp[i - coin] + 1)
            dp[i] = res
        return dp[-1] if dp[-1] != math.inf else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    result = sol.coinChange(coins, amount)
    print(result)
