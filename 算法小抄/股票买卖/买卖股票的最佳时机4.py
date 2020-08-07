"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""
import math
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfit_k_inf(prices):
            dp0, dp1 = 0, -math.inf
            for i in range(len(prices)):
                tmp = dp0
                dp0 = max(dp0, dp1 + prices[i])
                dp1 = max(dp1, tmp - prices[i])
            return dp0

        length = len(prices)
        # 卖出买入一共需要两天，所以最多只能
        if k > length / 2:
            return maxProfit_k_inf(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(length)]
        for i in range(length):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][k][0]


if __name__ == '__main__':
    prices = [1,2]
    k = 1
    sol = Solution()
    result = sol.maxProfit(k, prices)
    print(result)
